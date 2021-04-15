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
			// console.log("value: ", value, " key: ", key);
			if (key == "village") {
				let datosVilla = [];
				datosVilla = value;
				// console.log("entro aquí", datosVilla);
				return datosVilla;
			}
		}
	};
	let villaData = villageData(userVillage);
	console.log("la variable que devuelve la funcion: ", villaData);

	// {Object.keys(data.tasks).map((date) => {
	//     const dayTasks = tasks[date];
	//     return Object.keys(dayTasks).map((key) => {
	//         const task = dayTasks[key];
	//         return (
	//           <li>{task.name}</li>
	//         )
	//     })
	// })}

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
						{/* Otro intento fallido: */}
						{/* <ul>
							{Object.keys(villaData).map(item => {
								const clavesVillas = villa[item];
								return Object.keys(clavesVillas).map(key => {
									const villa = clavesVillas[key];
									return <li key={key}>{villa.name}</li>;
								});
							})}
						</ul> */}

						{/* <h4> Tu enlace es:</h4>
						<strong>{store.village}</strong>
						<br />
						<h4> Tu teléfono de contacto:</h4>
						<strong>{store.village.phone}</strong>
						<br />
						<h4>Hace entregas y recogidas en:</h4> */}

						{/* <strong>ALBERGUE DE {villageData()}, este es mi id:</strong> */}
						<br />
					</div>
				</div>
			</div>
			<h3>Echa un vistazo a nuestras estanterías</h3>
		</div>
	);
};
