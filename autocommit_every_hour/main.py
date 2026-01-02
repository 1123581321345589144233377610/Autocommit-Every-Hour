if __name__ == '__main__':
    import autocommit
    import schedule
    import time

    schedule.every().hour.do(autocommit.create_empty_commit)
    autocommit.create_empty_commit()
    while True:
        schedule.run_pending()
        time.sleep(60)