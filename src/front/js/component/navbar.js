import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
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
			</div>
		</nav>
	);
};
