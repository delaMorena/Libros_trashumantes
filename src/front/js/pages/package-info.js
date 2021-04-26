import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { NoToken } from "../component/no-token";
import { useParams } from "react-router-dom";

export const PackageInfo = () => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	useEffect(
		() => {
			actions.getUser();
			actions.getPack(params.id);
			//habrá que traerse los libros
			//POST reservas
			// get Reviews
			// post reviews if lo reservaste
		},
		[store.token]
	);
	if (store.token == null) {
		console.log(store.token);

		return <NoToken />;
	} else {
		return (
			<div className="container">
				<div className="col-6">
					{Object.keys(store.onePack).length == 0 ? (
						"no estoy"
					) : (
						<div>
							<h4> {store.onePack.package_tittle} </h4>
						</div>
					)}
				</div>
				<div>libros que contiene</div>
				<div>reservado o no</div>
				<div>opiniones</div>
				<div>publicar una opinión</div>
			</div>
		);
	}
};
