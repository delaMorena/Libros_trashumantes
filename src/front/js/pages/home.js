import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";
import mountains from "../../img/homelandscape.jpeg";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<div className="bg-mountains">
				<div>
					<h1>Eres del Valle de Tena </h1>
					<h1>Te gusta leer </h1>
					<h4 className="mt-5">Resides en algún pueblo de la Comarca Alto-Gállego</h4>
					<h4>Pero todas las bibliotecas están cerradas o sus horarios no te cuadran...</h4>
				</div>
				<div />
			</div>

			<div className="mt-1 row justify-content-center bg-books">
				<div className="col-4 pseudomodal">
					<h2>¿Como funciona libros trashumantes?</h2>
				</div>
			</div>
		</div>
	);
};
