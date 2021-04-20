import React, { useContext, useState } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import { useHistory } from "react-router-dom";
import "../../styles/forms.scss";
import { CoolKidsSitting } from "../../img/CoolKidsSitting.png";

export const SignUp = () => {
	const { store, actions } = useContext(Context);

	const history = useHistory();

	const [firstName, setFirstName] = useState("mozica");
	const [lastName, setLastName] = useState("moza");
	const [age, setAge] = useState("34");
	const [email, setEmail] = useState("moz@ano");
	const [password, setPassword] = useState("123");
	const [dni, setDni] = useState("1234");
	const [village, setVillage] = useState(1);

	const params = useParams();

	const HandleClickLogin = () => {
		const payload = {
			email: email,
			password: password,
			firstName: firstName,
			lastName: lastName,
			dni: dni,
			age: age,
			village: village
		};
		if (store.token) {
			actions.updateUser(payload, () => {
				history.push("/");
			});
		} else {
			actions.createUser(payload, () => {
				history.push("/");
			});
		}
	};

	return (
		<div className="container-fluid register pb-5">
			<div className="row ">
				<div className="col-lg-6 col-12 register-izq">
					<div className="text-center my-3">
						<h1>{store.token ? "Modifica tus datos" : "Por favor rellena tus datos"}</h1>
					</div>
					<div className="col-lg-12 col-xs-12  register-izq-inside ">
						<form>
							<div className="">
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
							<div className="">
								<label className="form-label">DNI</label>
								<input
									type="text"
									className="form-control"
									value={dni}
									onChange={event => setDni(event.target.value)}
								/>
							</div>
							<div className="">
								<label className="form-label">Edad de la persona que leerá los libros</label>
								<input
									type="text"
									className="form-control"
									value={age}
									onChange={event => setAge(event.target.value)}
								/>
							</div>
							<div className="">
								<label className="form-label">Correo electrónico</label>
								<input
									type="email"
									className="form-control"
									value={email}
									onChange={event => setEmail(event.target.value)}
								/>
							</div>
							<div className="">
								<label className="form-label">Contraseña</label>
								<input
									type="password"
									className="form-control"
									value={password}
									onChange={event => setPassword(event.target.value)}
								/>
							</div>
							<div className="">
								<label className="form-label">Pueblo</label>
								<input
									type="text"
									className="form-control"
									value={village}
									onChange={event => setVillage(event.target.value)}
								/>
							</div>
							{/* <div className="">
					<label className="form-label">Repite Contraseña</label>
					<input
						type="password"
						className="form-control"
						value={confirmPassword}
						onChange={event => setConfirmPassword(event.target.value)}
					/>
				</div> */}

							<button type="button" className="btn btn-primary mt-4" onClick={HandleClickLogin}>
								{store.token ? "Actualizar datos" : "Registrarse"}
							</button>
						</form>
					</div>
				</div>
				<div className="col-lg-6 .d-sm-none .d-md-none register-der">
					<div className=" register-der-inside" />
				</div>
			</div>
		</div>
	);
};
