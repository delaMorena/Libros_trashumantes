import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { useHistory } from "react-router-dom";

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
			}
		});
	}

	return (
		<div>
			Inicia sesión
			<form>
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
				<button type="button" className="btn btn-primary" onClick={() => handleSubmit()}>
					Submit
				</button>
			</form>
		</div>
	);
};
