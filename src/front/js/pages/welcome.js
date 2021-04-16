import React, { useContext, useState, useEffect } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Welcome = () => {
	const { store, actions } = useContext(Context);
	let userVillage = store.user;
	console.log(userVillage);

	useEffect(() => {
		actions.getUser();
		// await actions.getUser(); igual así para que traiga la información
		console.log("user despues de getUser: ", store.user);
	}, []);

	// const villageData = obj => {
	// 	for (const [key, findVillainObject] of Object.entries(obj)) {
	// 		if (key == "village") {
	// 			return findVillainObject;
	// 		}
	// 	}
	// };
	// let villaData = villageData(userVillage);
	// const pintarPueblo = obj => {
	// 	if (obj == undefined || obj == null) {
	// 		return <h2> Un momentito</h2>;
	// 	} else {
	// 		console.log("he entrado, pintarpueblo entra al else", obj.volunteer);
	// 		return (
	// 			<div>
	// 				<h4>
	// 					{" "}
	// 					Tu enlace es:
	// 					{store.user.village.volunteer}{" "}
	// 				</h4>
	// 				<strong>{obj.volunteer}</strong>
	// 				<br />
	// 				<h4> Su teléfono de contacto:</h4>
	// 				<strong>{obj.phone}</strong>
	// 				<br />
	// 				<h4>Hace entregas y recogidas en:</h4>
	// 				<strong>ALBERGUE DE {obj.village_name}</strong>
	// 				<br />
	// 			</div>
	// 		);
	// 	}
	// };
	// let finalVilla = pintarPueblo(villaData);

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
						{Object.keys(store.user).length == 0 ? (
							""
						) : (
							<div>
								<h4> Tu enlace es: </h4>
								<strong>{store.user.village.volunteer}</strong>
								<br />
								<h4> Su teléfono de contacto:</h4>
								<strong>{store.user.village.phone}</strong>
								<br />
								<h4>Hace entregas y recogidas en:</h4>
								<strong>ALBERGUE DE {store.user.village.village_name}</strong>
								<br />
							</div>
						)}
					</div>
				</div>
			</div>
			<Link to="/shelves">
				<h4>Echa un vistazo a nuestras estanterías</h4>
			</Link>
		</div>
	);
};
// {Object.keys(store.user).length == 0
// 							? ""
// 							: Object.keys(store.user.village).map((value, index) => {
// 									return (
// 										<div key={index}>
// 											<h2>{value + ": "}</h2>
// 											<h4> {store.user[value]}</h4>
// 										</div>
// 									);
// 							  })}
