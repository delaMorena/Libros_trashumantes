import React, { useContext, useEffect } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import logoprov from "../../img/logoprov.png";

export const Navbar = () => {
	const { store, actions } = useContext(Context);

	useEffect(
		() => {
			actions.getUser();
		},
		[store.token]
	);
	if (store.token == null) {
		return (
			<nav className="navbar navbar-expand-lg navbar-light">
				<Link className="navbar-brand" to="/">
					<img src={logoprov} className="d-inline-block align-top style-logo-navbar" alt="logo" width="100" />
					Libros Trashumantes
				</Link>
				<button
					className="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarNavDropdown"
					aria-controls="navbarNavDropdown"
					aria-expanded="false"
					aria-label="Toggle navigation">
					<span className="navbar-toggler-icon" />
				</button>
				<div className="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
					<ul className="navbar-nav style-ul-navbar dropdown-menu-right">
						<li className="nav-item">
							<Link to="/login">
								<button type="button" className="btn login-button-style mx-1">
									Entrar
								</button>
							</Link>
						</li>
						<li className="nav-item">
							<Link to="/signup">
								<button type="button" className="btn register-button-style-navbar mx-1">
									Registrarme
								</button>
							</Link>
						</li>
						{/* <li className="nav-item">
							<Link className="nav-link" to="/about-us">
								Quienes somos
							</Link>
						</li> */}
					</ul>
				</div>
			</nav>
		);
	} else {
		return (
			<nav className="navbar navbar-expand-lg navbar-light">
				<Link className="navbar-brand" to="/">
					<img src={logoprov} className="d-inline-block align-top style-logo-navbar" alt="logo" width="100" />
					Libros Trashumantes
				</Link>
				<button
					className="navbar-toggler"
					type="button"
					data-toggle="collapse"
					data-target="#navbarNavDropdown"
					aria-controls="navbarNavDropdown"
					aria-expanded="false"
					aria-label="Toggle navigation">
					<span className="navbar-toggler-icon" />
				</button>
				<div className="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
					<ul className="navbar-nav style-ul-navbar">
						<li className="nav-item active">
							<Link className="nav-link" to="/shelves">
								Estanterías
								<span className="sr-only">(current)</span>
							</Link>
						</li>
						<li className="nav-item">
							<Link className="nav-link" to="/welcome">
								Enlace
							</Link>
						</li>
						<li className="nav-item dropdown color-username">
							<a
								className="nav-link dropdown-toggle"
								href="#"
								id="navbarDropdownMenuLink"
								data-toggle="dropdown"
								aria-haspopup="true"
								aria-expanded="false">
								{store.user.email}
							</a>
							<div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
								<Link
									className="dropdown-item"
									to="/bye"
									type="button"
									onClick={() => actions.logOut()}
									style={{ color: "grey" }}>
									Cerrar sesión
								</Link>
							</div>
						</li>
					</ul>
				</div>
			</nav>
		);
	}
};

// //// aquí empieza mi código:
// 	return (
// 		<nav className="navbar navbar-light bg-light mb-3">
// 			<Link to="/">
// 				<span className="navbar-brand mb-0 h1">Libros Trashumantes</span>
// 			</Link>
// 			<div className="ml-auto">
// 				<Link to="/signup">
// 					<button className="btn btn-primary mx-2">Registrate</button>
// 				</Link>
// 				<Link to="/login">
// 					<button className="btn btn-primary mx-2">Inicia sesión</button>
// 				</Link>
// 				<Link
// 					className="btn btn-succes mx-2"
// 					to="/bye"
// 					type="button"
// 					onClick={() => actions.logOut()}
// 					style={{ color: "grey" }}>
// 					Cerrar sesión
// 				</Link>
// 				<Link to="/welcome">
// 					<button className="btn btn-primary mx-2">Tu enlace</button>
// 				</Link>
// 			</div>
// 		</nav>
// 	);
// };
