import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";

export const SignUp = () => {
	const { store, actions } = useContext(Context);

	const [firstName, setFirstName] = useState("mozica");
	const [lastName, setLastName] = useState("moza");
	const [age, setAge] = useState("34");
	const [email, setEmail] = useState("moz@ano");
	const [password, setPassword] = useState("123");
	// const [confirmPassword, setConfirmPassword] = useState("123");
	const [dni, setDni] = useState("1234");
	const [village, setVillage] = useState(1);

	const HandleClick = () => {
		// console.log({
		// 	email: email,
		// 	firstName: firstName,
		// 	lastName: lastName,
		// 	age: age,
		// 	dni: dni,
		// 	password: password,
		// 	confirmPassword: confirmPassword
		// });

		const payload = {
			email: email,
			password: password,
			firstName: firstName,
			lastName: lastName,
			dni: dni,
			age: age,
			village: village
		};
		actions.createUser(payload);
	};

	return (
		<div className="m-auto">
			<h1>Regístrate</h1>
			<form>
				<div className="mb-3">
					<label className="form-label">Nombre</label>
					<input
						type="text"
						className="form-control"
						value={firstName}
						onChange={event => setFirstName(event.target.value)}
					/>
					<label className="form-label">Apellidos</label>
					<input
						type="text"
						className="form-control"
						value={lastName}
						onChange={event => setLastName(event.target.value)}
					/>
				</div>
				<div className="mb-3">
					<label className="form-label">DNI</label>
					<input
						type="text"
						className="form-control"
						value={dni}
						onChange={event => setDni(event.target.value)}
					/>
				</div>
				<div className="mb-3">
					<label className="form-label">Edad de la persona que leerá los libros</label>
					<input
						type="text"
						className="form-control"
						value={age}
						onChange={event => setAge(event.target.value)}
					/>
				</div>
				<div className="mb-3">
					<label className="form-label">Correo electrónico</label>
					<input
						type="email"
						className="form-control"
						value={email}
						onChange={event => setEmail(event.target.value)}
					/>
				</div>
				<div className="mb-3">
					<label className="form-label">Contraseña</label>
					<input
						type="password"
						className="form-control"
						value={password}
						onChange={event => setPassword(event.target.value)}
					/>
				</div>
				<div className="mb-3">
					<label className="form-label">Pueblo</label>
					<input
						type="number"
						className="form-control"
						value={village}
						onChange={event => setVillage(event.target.value)}
					/>
				</div>
				{/* <div className="mb-3">
					<label className="form-label">Repite Contraseña</label>
					<input
						type="password"
						className="form-control"
						value={confirmPassword}
						onChange={event => setConfirmPassword(event.target.value)}
					/>
				</div> */}

				<button type="submit" className="btn btn-primary" onClick={HandleClick}>
					Registrarse
				</button>
			</form>
		</div>
	);
};
