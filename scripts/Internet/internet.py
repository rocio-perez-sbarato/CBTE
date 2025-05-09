from scraping.internet_claro import obtener_primer_plan_claro
from scraping.internet_movistar import obtener_primer_plan_movistar
from scraping.internet_personal import obtener_primer_plan_personal
from utils.archivos import guardar_en_excel
from utils.rendimiento import medir_recursos
import logging
import logging.config

logging.config.fileConfig('logging_config/logging.conf')
logger = logging.getLogger('root')

def main():
    with medir_recursos():
        logger.info("===========INICIANDO SCRAPING DE TELEFONIA===========\n")

        try:
            logger.debug("Obteniendo primer plan de Personal")
            plan_personal = obtener_primer_plan_personal()
            logger.info(f"Plan Personal obtenido: {plan_personal}")
            guardar_en_excel(plan_personal)
            logger.debug("Plan Personal guardado en Excel")
        except Exception as e:
            logger.error(f"Error al obtener o guardar plan Personal: {e}")

        try:
            logger.debug("Obteniendo primer plan de Movistar")
            plan_movistar = obtener_primer_plan_movistar()
            logger.info(f"Plan Movistar obtenido: {plan_movistar}")
            guardar_en_excel(plan_movistar)
            logger.debug("Plan Movistar guardado en Excel")
        except Exception as e:
            logger.error(f"Error al obtener o guardar plan Movistar: {e}")

        try:
            logger.debug("Obteniendo primer plan de Claro")
            plan_claro = obtener_primer_plan_claro()
            logger.info(f"Plan Claro obtenido: {plan_claro}")
            guardar_en_excel(plan_claro)
            logger.debug("Plan Claro guardado en Excel")
        except Exception as e:
            logger.error(f"Error al obtener o guardar plan Claro: {e}")

    logger.info("===========SCRAPING DE TELEFONIA FINALIZADO===========\n")


if __name__ == "__main__":
    main()




    