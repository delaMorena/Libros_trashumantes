import React, { useContext, useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Context } from "../store/appContext";
import { useHistory } from "react-router-dom";
import "../../styles/forms.scss";

export const SignUp = () => {
	const { store, actions } = useContext(Context);

	const history = useHistory();

	const [firstName, setFirstName] = useState("Silvia");
	const [lastName, setLastName] = useState("Giao");
	const [age, setAge] = useState("41");
	const [email, setEmail] = useState("silvia@giao.au");
	const [password, setPassword] = useState("123");
	const [dni, setDni] = useState("56789321");
	const [village, setVillage] = useState(1);

	const params = useParams();

	useEffect(() => {
		actions.getVillages();
	}, []);

	const showVillageOption = () => {
		const villageOption = store.villages.map((village, index) => {
			return (
				<option key={index} value={village.id}>
					{village.village_name}
				</option>
			);
		});
		if (store.villages.length == 0) {
			return (
				<>
					<option>No se han encontrado pueblos</option>
				</>
			);
		} else {
			return villageOption;
		}
	};

	const HandleClickLogin = () => {
		const payload = {
			email: email,
			password: password,
			firstName: firstName,
			lastName: lastName,
			dni: dni,
			age: parseInt(age),
			village: parseInt(village)
		};
		console.log("age: ", typeof payload.age, "village: ", typeof payload.village);
		if (store.token) {
			actions.updateUser(payload, () => {
				history.push("/");
			});
		} else {
			actions.createUser(payload, () => {
				history.push("/welcome");
			});
		}
	};

	return (
		<div className="container-fluid register pb-5">
			<div className="register-izq">
				<h2 className="title-signup">{store.token ? "Modifica tus datos" : "Por favor rellena tus datos"}</h2>
				<form>
					<div className="row register-izq-inside ">
						<div className="col-5">
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
							<label className="form-label">Correo electrónico</label>
							<input
								type="email"
								className="form-control"
								value={email}
								onChange={event => setEmail(event.target.value)}
							/>

							<label className="form-label">DNI</label>
							<input
								type="text"
								className="form-control"
								value={dni}
								onChange={event => setDni(event.target.value)}
							/>
						</div>
						<div className="col-7">
							<label className="form-label">Edad de la persona que leerá los libros</label>
							<input
								type="text"
								className="form-control"
								value={age}
								onChange={event => setAge(event.target.value)}
							/>

							<label className="form-label">Contraseña</label>
							<input
								type="password"
								className="form-control"
								value={password}
								onChange={event => setPassword(event.target.value)}
							/>
							<select
								className="form-control inicio-input-style"
								onChange={e => setVillage(e.target.value)}>
								<option>Elige un pueblo</option>
								{showVillageOption()}
							</select>
						</div>
						<button type="button" className="register-button " onClick={HandleClickLogin}>
							{store.token ? "Actualizar datos" : "Registrarse"}
						</button>
					</div>
				</form>
			</div>
		</div>
	);
};
