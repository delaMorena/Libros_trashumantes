// const baseUrl = "https://3001-gold-cod-6w48l46i.ws-eu03.gitpod.io/api";

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			newUser: {}
		},
		actions: {
			createUser(input) {
				const store = getStore();
				const endpoint = "https://3001-gold-cod-6w48l46i.ws-eu03.gitpod.io/api/users";

				const method = "POST";
				const config = {
					method: method,
					headers: {
						"Content-Type": "application/json"
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
					.then(responseJson => {
						setStore({ newUser: responseJson });
						console.log("contacto", store.newUser);
					});
			}
		}
	};
};

export default getState;
