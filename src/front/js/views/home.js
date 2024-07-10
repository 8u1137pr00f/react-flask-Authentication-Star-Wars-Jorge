import React, { useContext, useEffect } from "react";
import "../../styles/home.css";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Home = () => {
    const { store, actions } = useContext(Context);

    useEffect(() => {
        actions.getCharacters();
        actions.getVehicles();
        actions.getPlanets();
    }, []);

    const createCarouselItems = (items, type) => {
        const slides = [];
        for (let i = 0; i < items.length; i += 4) {
            const chunk = items.slice(i, i + 4);
            slides.push(
                <div className={`carousel-item ${i === 0 ? "active" : ""}`} key={`slide-${type}-${i}`}>
                    <div className="row justify-content-center">
                        {chunk.map((item) => (
                            <div className="col-12 col-sm-6 col-md-4 col-lg-3" key={item.uid}>
                                <div className="card mx-2 mb-4" style={{ width: "100%" }}>
                                    <img
                                        src={`https://starwars-visualguide.com/assets/img/${type}/${item.uid}.jpg`}
                                        className="card-img-top"
                                        alt={item.name}
                                    />
                                    <div className="card-body">
                                        <h5 className="card-title">{item.name}</h5>
                                        <div className="d-flex justify-content-between">
                                            <Link to={`./${type}/${item.uid}`} className="btn btn-outline-dark">
                                                Learn more!
                                            </Link>
                                            <button
                                                className={`btn ms-2 ${store.favorites.some(fav => fav.uid === item.uid) ? 'btn-success' : 'btn-dark'}`}
                                                onClick={() => actions.toggleFavorite({ ...item, type })}>
                                                <i className="fas fa-globe"></i> +
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            );
        }
        return slides;
    };

    return (
        <div className="container">
            <h2 className="text-center">Characters</h2>
            <div id="charactersCarousel" className="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
                <div className="carousel-inner">
                    {createCarouselItems(store.validCharacters, "characters")}
                </div>
                <button className="carousel-control-prev custom-carousel-control position-absolute top-50" type="button" data-bs-target="#charactersCarousel" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next custom-carousel-control position-absolute top-50" type="button" data-bs-target="#charactersCarousel" data-bs-slide="next">
                    <span className="carousel-control-next-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>

            <h2 className="text-center">Vehicles</h2>
            <div id="vehiclesCarousel" className="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
                <div className="carousel-inner">
                    {createCarouselItems(store.validVehicles, "vehicles")}
                </div>
                <button className="carousel-control-prev custom-carousel-control position-absolute top-50" type="button" data-bs-target="#vehiclesCarousel" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next custom-carousel-control position-absolute top-50" type="button" data-bs-target="#vehiclesCarousel" data-bs-slide="next">
                    <span className="carousel-control-next-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>

            <h2 className="text-center">Planets</h2>
            <div id="planetsCarousel" className="carousel slide" data-bs-ride="carousel" data-bs-interval="5000">
                <div className="carousel-inner">
                    {createCarouselItems(store.validPlanets, "planets")}
                </div>
                <button className="carousel-control-prev custom-carousel-control position-absolute top-50" type="button" data-bs-target="#planetsCarousel" data-bs-slide="prev">
                    <span className="carousel-control-prev-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Previous</span>
                </button>
                <button className="carousel-control-next custom-carousel-control position-absolute top-50" type="button" data-bs-target="#planetsCarousel" data-bs-slide="next">
                    <span className="carousel-control-next-icon custom-carousel-icon" aria-hidden="true"></span>
                    <span className="visually-hidden">Next</span>
                </button>
            </div>
        </div>
    );
};