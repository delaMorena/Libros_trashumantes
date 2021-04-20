import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { NoToken } from "../component/no-token";

export const Shelves = () => {
	const { store, actions } = useContext(Context);

	if (store.token == null) {
		console.log(store.token);

		return <NoToken />;
	} else {
		return <div>estanterías</div>;
	}
};
