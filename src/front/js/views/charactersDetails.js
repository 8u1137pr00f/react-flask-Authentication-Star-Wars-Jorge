import React, { useContext, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import "../../styles/home.css";
import { Link } from "react-router-dom";

export const CharactersDetails = () => {
	const { store, actions } = useContext(Context);
	const { id } = useParams();

	useEffect(() => {
		actions.getCharactersDetails(id);
	}, [id]);

	return (
		<div className="d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
			<div className="card text-center" style={{ width: "18rem" }}>
				<img src={`https://starwars-visualguide.com/assets/img/characters/${id}.jpg`} className="card-img-top" alt="..." />
				<div className="card-body">
					<p className="card-text">Name: {store.characterDetails.name}</p>
					<p className="card-text">Birth year: {store.characterDetails.birth_year}</p>
					<p className="card-text">Gender: {store.characterDetails.gender}</p>
					<p className="card-text">Height: {store.characterDetails.height}</p>
					<p className="card-text">Skin color: {store.characterDetails.skin_color}</p>
					<p className="card-text">Hair color: {store.characterDetails.hair_color}</p>
					<Link to="/" className="btn btn-dark">Return to ship</Link>
				</div>
			</div>
		</div>
	);
};