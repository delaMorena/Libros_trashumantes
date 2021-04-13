import React, { useContext, useState, useEffect } from "react";
import { Context } from "../store/appContext";

export const Welcome = () => {
	const { store, actions } = useContext(Context);

	return (
		<div>
			<h1>¡Bienvenida Fulanita de tal!</h1>
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
						<h4> Tu enlace es:</h4>
						<strong>MARIBEL VERDÍN</strong>
						<br />
						<h4> Tu teléfono de contacto:</h4>
						<strong>665889003</strong>
						<br />
						<h4>Hace entregas y recogidas en:</h4>

						<strong>ALBERGUE DE PIEDRAFITA LOS PRIMEROS JUEVES DE CADA MES</strong>
						<br />
					</div>
				</div>
			</div>
			<h3>Echa un vistazo a nuestras estanterías</h3>
		</div>
	);
};
