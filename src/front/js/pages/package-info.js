import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { NoToken } from "../component/no-token";
import { useParams } from "react-router-dom";

export const PackageInfo = () => {
	const { store, actions } = useContext(Context);
	const params = useParams();

	useEffect(() => {
		actions.getUser();
		actions.getPack(params.id);

		//POST reservas
		// get Reviews
		// post reviews if lo reservaste
	}, []);

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
				<div>reservado o no</div>
				<div>opiniones</div>
				<div>publicar una opinión</div>
				<div>
					{store.books.map((book, index) => {
						console.log(book.author, index);
						<p key={index}>{book.author}</p>;
					})}
				</div>
			</div>
		);
	}
};
