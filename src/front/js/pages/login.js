import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { useHistory } from "react-router-dom";
import "../../styles/forms.scss";

export const LogIn = () => {
	const { store, actions } = useContext(Context);

	const history = useHistory();

	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");

	function handleSubmit() {
		const input = {
			email: email,
			password: password
		};
		actions.logIn(input, () => {
			if (store.error == null) {
				history.push("/");
			} else {
				history.push("/welcome");
			}
		});
	}
	// const HandleClick = async event => {
	// 	const payload = {
	// 		email: email,
	// 		password: password
	// 	};
	// 	await actions.userLogin(payload); // HASTA QUE NO SE EJECUTA ESTA FUNCION NO PASA A LA SIGUIENTE LINEA DE CODIGO

	// 	history.push("/inicio");
	// };

	return (
		<div className="register container">
			<h2 className="title-signup ">Inicia sesión</h2>
			<form className="login__form--dimensions login__form--pushfooter">
				<div className="mb-3">
					<label className="form-label" htmlFor="InputEmail">
						Email address
					</label>
					<input
						value={email}
						onChange={event => setEmail(event.target.value)}
						type="email"
						className="form-control"
						id="InputEmail"
						aria-describedby="emailHelp"
					/>
				</div>
				<div className="mb-3">
					<label htmlFor="InputPassword" className="form-label">
						Password
					</label>
					<input
						type="password"
						className="form-control"
						id="InputPassword"
						value={password}
						onChange={event => setPassword(event.target.value)}
					/>
				</div>
				<button type="button" className="register-button" onClick={() => handleSubmit()}>
					Submit
				</button>
			</form>
			{/* <div className="push-footer"> hola</div> */}
		</div>
	);
};
