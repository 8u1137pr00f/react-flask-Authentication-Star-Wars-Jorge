import React, { useContext, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Link } from "react-router-dom";

export const PlanetsDetails = () => {
	const { store, actions } = useContext(Context);
	const { id } = useParams();

	useEffect(() => {
		actions.getPlanetsDetails(id);
	}, [id]);

	if (id === "1" && store.invalidImages.includes("1")) {
		return (
			<div className="d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
				<div className="card text-center" style={{ width: "18rem" }}>
					<div className="card-body">
						<p className="card-text">Image for this planet is not available.</p>
						<Link to="/" className="btn btn-dark">Return to galaxy</Link>
					</div>
				</div>
			</div>
		);
	}

	return (
		<div className="d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
			<div className="card text-center" style={{ width: "18rem" }}>
				<img src={`https://starwars-visualguide.com/assets/img/planets/${id}.jpg`} className="card-img-top" alt="..." />
				<div className="card-body">
					<p className="card-text">Name: {store.planetsDetails.name}</p>
					<p className="card-text">Population: {store.planetsDetails.population} sentient beings</p>
					<p className="card-text">Gravity: {store.planetsDetails.gravity} G</p>
					<p className="card-text">Diameter: {store.planetsDetails.diameter} km</p>
					<p className="card-text">Climate details: {store.planetsDetails.climate}</p>
					<p className="card-text">Terrain details: {store.planetsDetails.terrain}</p>
					<p className="card-text">Water measurements: {store.planetsDetails.surface_water} %</p>
					<Link to="/" className="btn btn-dark">Return to galaxy</Link>
				</div>
			</div>
		</div>
	);
};