const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            users: [],
            characters: [],
            validCharacters: [],
            characterDetails: [],
            vehicles: [],
            validVehicles: [],
            vehiclesDetails: [],
            planets: [],
            validPlanets: [],
            planetsDetails: [],
            favorites: [],
            invalidImages: []
        },

        actions: {
            
            login: async(email, password) => {
                try {
                    let response = await fetch("https://curly-waddle-7v7r6qv67696crgg9-3001.app.github.dev/api/login", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json"
                        },
                        body: JSON.stringify({
                            "email": email,
                            "password": password
                        })

                    })

                    const data = await response.json()
                    localStorage.setItem("token", data.access_token);
                    return true

                }   catch (error) {
                    return false
                }
            },

            getCharacters: async () => {
                const res = await fetch(`https://www.swapi.tech/api/people/`);
                const data = await res.json();
                const validChars = await Promise.all(
                    data.results.map(async (item) => {
                        const isValid = await getActions().checkImageURL(`https://starwars-visualguide.com/assets/img/characters/${item.uid}.jpg`);
                        return isValid ? item : null;
                    })
                );
                setStore({ characters: data.results, validCharacters: validChars.filter(Boolean) });
            },
            getCharactersDetails: async (id) => {
                const result = await fetch(`https://www.swapi.tech/api/people/${id}`);
                const data = await result.json();
                setStore({ characterDetails: data.result.properties });
            },
            getVehicles: async () => {
                const res = await fetch(`https://www.swapi.tech/api/vehicles/`);
                const data = await res.json();
                const validVehs = await Promise.all(
                    data.results.map(async (item) => {
                        const isValid = await getActions().checkImageURL(`https://starwars-visualguide.com/assets/img/vehicles/${item.uid}.jpg`);
                        return isValid ? item : null;
                    })
                );
                setStore({ vehicles: data.results, validVehicles: validVehs.filter(Boolean) });
            },
            getVehiclesDetails: async (id) => {
                const result = await fetch(`https://www.swapi.tech/api/vehicles/${id}`);
                const data = await result.json();
                setStore({ vehiclesDetails: data.result.properties });
            },
            getPlanets: async () => {
                const res = await fetch(`https://www.swapi.tech/api/planets/`);
                const data = await res.json();
                const validPlts = await Promise.all(
                    data.results.map(async (item) => {
                        // Si la imagen es 1.jpg y está marcada como no válida, retornamos null
                        if (item.uid === "1" && getStore().invalidImages.includes("1")) return null;
                        const isValid = await getActions().checkImageURL(`https://starwars-visualguide.com/assets/img/planets/${item.uid}.jpg`);
                        return isValid ? item : null;
                    })
                );
                setStore({ planets: data.results, validPlanets: validPlts.filter(Boolean) });
            },
            getPlanetsDetails: async (id) => {
                const result = await fetch(`https://www.swapi.tech/api/planets/${id}`);
                const data = await result.json();
                setStore({ planetsDetails: data.result.properties });
            },
            checkImageURL: async (url) => {
                try {
                    const response = await fetch(url);
                    if (response.status === 404 && url.includes("1.jpg")) {
                        // Si la imagen es 1.jpg y da 404, la añadimos a la lista de imágenes no válidas
                        const invalidImages = getStore().invalidImages;
                        setStore({ invalidImages: [...invalidImages, "1"] });
                    }
                    return response.ok;
                } catch (error) {
                    console.error(`Error fetching image from ${url}:`, error);
                    return false;
                }
            },
            toggleFavorite: (item) => {
                const store = getStore();
                const favorites = store.favorites;
                const index = favorites.findIndex(fav => fav.uid === item.uid);

                if (index === -1) {
                    // Add
                    setStore({ favorites: [...favorites, item] });
                } else {
                    // Remove
                    const updatedFavorites = favorites.filter(fav => fav.uid !== item.uid);
                    setStore({ favorites: updatedFavorites });
                }
            },
            removeFavorite: (uid) => {
                const store = getStore();
                const updatedFavorites = store.favorites.filter(favorite => favorite.uid !== uid);
                setStore({ favorites: updatedFavorites });
            }
        }
    };
};

export default getState;