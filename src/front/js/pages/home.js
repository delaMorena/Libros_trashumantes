import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";
import mountains from "../../img/homelandscape.jpeg";
import { Link } from "react-router-dom";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<div className="bg-mountains">
				<div className="mt-3">
					<h1>Eres del Valle de Tena </h1>
					<h1>Te gusta leer </h1>
					<h4 className="mt-5">Resides en algún pueblo de la Comarca Alto-Gállego</h4>
					<h4>Pero todas las bibliotecas están cerradas o sus horarios no te cuadran...</h4>
				</div>
				<div />
			</div>

			<div className="mt-1 row  bg-books">
				<div className="col-5 pseudomodal">
					<h2 className="title-instructions">¿Como funciona LIBROS TRASHUMANTES?</h2>
					<ul className="instructions">
						<li> Te registras</li>
						<li> Eliges los paquetes de libros que te gustan</li>
						<li>
							Una persona responsable de los libros se pondrá en contacto contigo para llevártelos a tu
							punto de lectura más cercano
						</li>
						<li> Tendrás un mes para leerlo y releerlos</li>
						<li> Volveréis a quedar tu enlace y tú para devolver los libros</li>
					</ul>
					<Link to="/signup">
						<button className="call-to-action"> ¡Comienza a disfrutar de la lectura!</button>
					</Link>
				</div>
				<div className="push-footer" />
			</div>
		</div>
	);
};
