const baseUrl = process.env.BACKEND_URL;

const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {},
		actions: {
			createUser(input) {
				const endpoint = `${baseUrl}/users`;
				const method = "POST";
				const config = {
					method: method,
					headers: { "Content-Type": "application/json" },
					body: JSON.stringify({
						first_name: input.firstName,
						last_name: input.lastName,
						email: input.email,
						password: input.password,
						username: input.username
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
			}
		}
	};
};

export default getState;
