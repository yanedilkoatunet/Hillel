import logging


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    success - успішний вхід, рівень INFO
    expired - застарілий пароль, рівень WARNING
    failed - неправильний пароль, рівень ERROR
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    logging.basicConfig(
        filename="login_system.log",
        level=logging.INFO,
        format="%(asctime)s - %(message)s"
    )

    logger = logging.getLogger("log_event")

    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
