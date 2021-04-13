// const baseUrl = "https://3001-aquamarine-capybara-rmjshrbs.ws-eu03.gitpod.io/api";

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {},
		actions: {
			createUser(input) {
				const endpoint = "https://3001-rose-urial-vp1jy9ao.ws-eu03.gitpod.io/api/users";

				const method = "POST";
				const config = {
					method: method,
					headers: { "Content-Type": "application/json" },
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
						console.log(response);
						return response.json();
					})
					.then(json => {
						console.log(json);
					});
				// console.log("input: ", input);
			}
		}
	};
};

export default getState;
