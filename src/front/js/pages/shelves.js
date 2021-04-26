import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { NoToken } from "../component/no-token";
import { Link } from "react-router-dom";
import { PackageCard } from "../component/package-card";

export const Shelves = () => {
	const { store, actions } = useContext(Context);

	useEffect(() => {
		actions.getPackages();
	}, []);

	const cardItem = store.packages.map((pack, index) => {
		console.log(pack);
		return <PackageCard key={index} pack={pack} />;
	});

	if (store.token == null) {
		console.log(store.token);

		return <NoToken />;
	} else {
		return (
			<div className="container">
				<div className="row">
					<div className="col-md-7 offset-lg-4 col-10 offset-md-3">
						<h1>Asociaciones de ER</h1>
					</div>
					<div className="col-12 my-3">
						<p>Elige el paquete que quieras recibir en tu pueblo:</p>
					</div>
				</div>
				<hr />
				<div className="row justify-content-center mx-1">{cardItem}</div>
				<hr />
				<div className="row">
					<div className="col-12 text-center">
						<p>
							¿Te interesaría algún libro y no lo encuentras, algún otro tema que eches en falta?
							¡Solicitalo!
						</p>
					</div>
					<div className="col-12 text-center my-3">
						<Link to="/request/association">
							<button type="button" className="btn">
								Crear solicitud
							</button>
						</Link>
					</div>
				</div>
			</div>
		);
	}
};
