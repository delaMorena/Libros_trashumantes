import React, { useContext, useEffect } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";

export const Navbar = () => {
	const { store, actions } = useContext(Context);
	return (
		<nav className="navbar navbar-light bg-light mb-3">
			<Link to="/">
				<span className="navbar-brand mb-0 h1">Libros Trashumantes</span>
			</Link>
			<div className="ml-auto">
				<Link to="/signup">
					<button className="btn btn-primary mx-2">Registrate</button>
				</Link>
				<Link to="/login">
					<button className="btn btn-primary mx-2">Inicia sesión</button>
				</Link>
				<Link
					className="btn btn-succes mx-2"
					to="/bye"
					type="button"
					onClick={() => actions.logOut()}
					style={{ color: "grey" }}>
					Cerrar sesión
				</Link>
				<Link to="/welcome">
					<button className="btn btn-primary mx-2">Tu enlace</button>
				</Link>
			</div>
		</nav>
	);
};
