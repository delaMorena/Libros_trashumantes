import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.scss";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<div>
				<h1>Te gusta leer </h1>
				<h3>Pero todas las bibliotecas están cerradas o sus horarios no te cuadran...</h3>
			</div>
			<div>
				<h1>Eres del Valle de Tena </h1>
				<h3>Resides en algún pueblo de la Comarca Alto-Gállego</h3>
			</div>
			<div className="mt-5">
				<h2>¿Como funciona libros trashumantes?</h2>
			</div>
		</div>
	);
};
