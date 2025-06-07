# Extracting ERROR lines from server.log
with open("server.log", "r") as logfile, open("errors.log", "w") as errorfile:
    for line in logfile:
        if "ERROR" in line:
            errorfile.write(line)

print("Error lines written to 'errors.log'.")

