import React, { useState } from "react";

export const LogIn = () => {
	return (
		<div>
			Inicia sesión
			<form>
				<div className="mb-3">
					<label className="form-label">Email address</label>
					<input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
				</div>
				<div className="mb-3">
					<label htmlFor="exampleInputPassword1" className="form-label">
						Password
					</label>
					<input type="password" className="form-control" id="exampleInputPassword1" />
				</div>
				<button type="submit" className="btn btn-primary">
					Submit
				</button>
			</form>
		</div>
	);
};
