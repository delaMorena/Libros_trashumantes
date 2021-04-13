const baseUrl = "https://3001-blue-gopher-lg9tz1z7.ws-eu03.gitpod.io/api";

const getState = ({ getStore, getActions, setStore }) => {
	const token = localStorage.getItem("token");
	return {
		store: {
			user: [],
			token: token,
			error: null
		},
		actions: {
			createUser(input, callback) {
				const endpoint = `${baseUrl}/users`;

				const method = "POST";
				const config = {
					method: method,
					headers: {
						"Content-Type": "application/json",
						"Access-Control-Allow-Origin": "*"
					},
					body: JSON.stringify({
						first_name: input.firstName,
						last_name: input.lastName,
						email: input.email,
						password: input.password,
						dni: input.dni,
						age: input.age,
						village: input.village
					})
				};
				fetch(endpoint, config)
					.then(response => {
						return response.json();
					})
					.then(json => {
						setStore({ token: json.token });

						localStorage.setItem("token", json.token);
						callback(); //por qué este callback()???
					})
					.catch(error => {
						console.log(error);
					});
			},
			logIn(input, callback) {
				const endpoint = `${baseUrl}/login`;
				const config = {
					method: "POST",
					body: JSON.stringify({
						email: input.email,
						password: input.password
					}),
					headers: {
						"Content-Type": "application/json",
						"Access-Control-Allow-Origin": "*"
					}
				};
				fetch(endpoint, config)
					.then(response => {
						if (response.status == 403) {
							setStore({ error: response });
							return response.json();
						}
						setStore({ error: null });
						return response.json();
					})
					.then(json => {
						setStore({ token: json.token });
						localStorage.setItem("token", json.token);
						callback();
					})
					.catch(error => {
						setStore(error);
					});
			},
			logOut() {
				localStorage.removeItem("token");
				setStore({ token: null });
			},

			async getUser() {
				const store = getStore();
				const endpoint = `${baseUrl}/test`;
				const method = "GET";
				const headers = { "Content-Type": "application/json" };

				if (store.token) {
					headers["Authorization"] = `Bearer ${store.token}`;
				}

				const config = {
					method: method,
					headers: headers
				};
				await fetch(endpoint, config)
					.then(response => response.json())
					.then(data => {
						setStore({ user: data });
						console.log("contacto", store.user);
					});
			}
		}
	};
};

export default getState;
