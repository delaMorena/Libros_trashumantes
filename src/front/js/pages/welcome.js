import React, { useContext, useState, useEffect } from "react";
import { Context } from "../store/appContext";

export const Welcome = () => {
	const { store, actions } = useContext(Context);
	let userVillage = store.user;
	console.log(userVillage);

	useEffect(() => {
		actions.getUser();
		console.log("user despues de getUser: ", store.user);
	}, []);

	const villageData = obj => {
		for (const [key, value] of Object.entries(obj)) {
			if (key == "village") {
				let findVillainObject;
				findVillainObject = value;
				return findVillainObject;
			}
		}
	};
	let villaData = villageData(userVillage);
	const pintarPueblo = obj => {
		if (obj == undefined || obj == null) {
			return <h2> Un momentito</h2>;
		} else {
			console.log("he entrado, pintarpueblo entra al else", obj.volunteer);
			return (
				<div>
					<h4> Tu enlace es:</h4>
					<strong>{obj.volunteer}</strong>
					<br />
					<h4> Su teléfono de contacto:</h4>
					<strong>{obj.phone}</strong>
					<br />
					<h4>Hace entregas y recogidas en:</h4>
					<strong>ALBERGUE DE {obj.village_name}</strong>
					<br />
				</div>
			);
		}
	};
	let finalVilla = pintarPueblo(villaData);

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
					<div className="col-6">{finalVilla}</div>
				</div>
			</div>
			<h3>Echa un vistazo a nuestras estanterías</h3>
		</div>
	);
};
