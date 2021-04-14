import React, { useContext, useState, useEffect } from "react";
import { Context } from "../store/appContext";

export const Welcome = () => {
	const { store, actions } = useContext(Context);

	useEffect(() => {
		actions.getUser();
		console.log("user: ", store.user);

		actions.getVillage(1);
		console.log("store.village estoy??: ", store.village);
	}, []);

	return (
		<div>
			<h1>¡Bienvenida {store.user.first_name}!</h1>
			<div className="container">
				<div className="row">
					<div className="col-6">
						<img
							src="https://blush.design/api/download?shareUri=SgObsXSwnsOkHMhP&c=Skin_0%7Eedb98a&w=800&h=800&fm=png"
							alt="welcome-pic"
							width="300"
						/>
					</div>
					<div className="col-6">
						{/* <h4> Tu enlace es:</h4>
						<strong>{store.village}</strong>
						<br />
						<h4> Tu teléfono de contacto:</h4>
						<strong>{store.village.phone}</strong>
						<br />
						<h4>Hace entregas y recogidas en:</h4>

						<strong>
							ALBERGUE DE {store.village.village_name}, este es mi id: {store.user.village} LOS PRIMEROS
							JUEVES DE CADA MES
						</strong> */}
						<br />
					</div>
				</div>
			</div>
			<h3>Echa un vistazo a nuestras estanterías</h3>
		</div>
	);
};
