import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";
import mountains from "../../img/homelandscape.jpeg";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<div className="row">
				<div className="col-6 pl-5 pt-5 d-flex align-content-center flex-wrap">
					<div>
						<h1>Eres del Valle de Tena </h1>
						<h3>Resides en algún pueblo de la Comarca Alto-Gállego</h3>
					</div>
					<div>
						<h1>Te gusta leer </h1>
						<h3>Pero todas las bibliotecas están cerradas o sus horarios no te cuadran...</h3>
					</div>
				</div>
				<div className="bg-mountains col-6" />
			</div>
			<div className="mt-5 row justify-content-center bg-books">
				<div className="col-4 pseudomodal">
					<h2>¿Como funciona libros trashumantes?</h2>
				</div>
			</div>
		</div>
	);
};
