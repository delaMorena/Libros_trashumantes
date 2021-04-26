// PLANTILLA PARA MOSTRAR UN RESUMEN DE LOS PAQUETES DISPONIBLES O ALQUILADOS
import React from "react";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

export const PackageCard = props => {
	// recordar insertar props como parametro
	const { pack } = props;

	return (
		<div className="widthListItem my-4">
			<div className="card-body">
				<h5 className="card-title text-center py-2 bold">{pack.package_tittle}</h5>
				<h6 className="card-subtitle pb-4 text-muted text-center">{pack.suitable_ages} años</h6>

				<p className="card-text text-justify">{pack.package_description}</p>
				<div className="row mt-4 justify-content-between">
					<div className="col-6 text-left">
						<Link to={`/package-info/${pack.id}`}>
							<button type="button" className="btn btn-info btn-lg">
								Más información
							</button>
						</Link>
					</div>
					<p>{pack.reserved_status ? <p>Reservado</p> : <p> No Reservado</p>}</p>
				</div>
			</div>
		</div>
	);
};

PackageCard.propTypes = {
	pack: PropTypes.object
};
