import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import starWarsLogo from "../img/star_wars_logo_PNG28.png"; // Asegúrate de que la ruta sea correcta

export const Navbar = () => {
    const { store, actions } = useContext(Context);

    return (
        <nav className="navbar p-3 m-3" style={{ backgroundColor: 'rgba(0, 0, 0, 0.8)' }}>
            <Link to="/">
                <img src={starWarsLogo} alt="Star Wars Logo" style={{ height: "75px" }} className="navbar-brand mb-0 h1" />
            </Link>
            <div className="ms-auto">
                <div className="dropdown">
                    <button className="btn btn-dark dropdown-toggle btn-lg" type="button" id="favoritesDropdown" data-bs-toggle="dropdown" aria-expanded="false">
                        Favorites
                    </button>
                    <ul className="dropdown-menu dropdown-menu-end" aria-labelledby="favoritesDropdown">
                        {store.favorites.length === 0 ? (
                            <li><span className="dropdown-item">No favorites added</span></li>
                        ) : (
                            store.favorites.map((favorite, index) => (
                                <li key={index} className="d-flex justify-content-between align-items-center">
                                    <Link to={`/${favorite.type}/${favorite.uid}`} className="dropdown-item">
                                        {favorite.name}
                                    </Link>
                                    <button 
                                        className="btn btn-danger btn-sm mx-2" 
                                        onClick={() => actions.removeFavorite(favorite.uid)}>
                                        &times;
                                    </button>
                                </li>
                            ))
                        )}
                    </ul>
                </div>
            </div>
        </nav>
    );
};