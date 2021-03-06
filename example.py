import ltrtml

"""
example.py - Example dictionaries for sending observations to the Liverpool telescope
"""

# Settings Dictionary
settings = {
    'username': '',  # RTML_username
    'password': '',  # RTML_password
    'project': '',   # RTML_proposal name
    'prefix': '',    # Prefix to Group UID
    'LT_HOST': '',   # IP used to connect to the LT
    'LT_PORT': '',   # Port used to connect to the LT
    'DEBUG': False,  # Store all RTML responses for debugging, [True, False]
    'PKLFILE': '',   # Name of pickle file for storing observations
}

target1 = {
    'name': 'Vega',          # Target name
    'RA': '18:36:56.336',    # Target ra 'HH:MM:SS.SS'
    'DEC': '+38:47:01.280',  # Target dec '+/-DD:MM:SS.SS'
}

target2 = {
    'name': 'Deneb',         # Target name
    'RA': '20:41:25.915',    # Target ra 'HH:MM:SS.SS'
    'DEC': '+45:16:49.220',  # Target dec '+/-DD:MM:SS.SS'
}

constraints = {
    'air_mass': '2.0',            # Maximum allowable Airmass Range 1 --> 3
    'sky_bright': '2.0',          # Maximum allowable Sky Brightness, Dark + X magnitudes
    'seeing': '1.2',              # Maximum allowable FWHM seeing in arcsec
    'photometric': 'yes',         # Photometric conditions, ['yes', 'no']
    'start_date': '2020-02-18',   # Start Date 'YYYY-MM-DD'
    'start_time': '18:00:00.00',  # Start Time 'HH:MM:SS.SS'
    'end_date': '2020-02-28',     # End Date 'YYYY-MM-DD'
    'end_time': '00:00:00.00',    # End Time 'HH:MM:SS.SS'
}

# IOO Example observation with target1
observationIOO = {
    'instrument': 'IO:O',
    'target': target1,
    'filters': {'R': {'exp_time': '60',
                      'exp_count': '3',
                      },
                'U': {'exp_time': '45',
                      'exp_count': '3',
                      },
                },   # Select the filter/s for the IO:O observation,
                     # see list of filters below for acceptable filters
    'binning': '2',  # Binning '2' recommended. ['1', '2']
}

# Tuple of valid IOO filters for reference;
ioo_filters = ['U',
               'R',
               'G',
               'I',
               'Z',
               'B',
               'V',
               'Halpha6566',
               'Halpha6634',
               'Halpha6705',
               'Halpha6755',
               'Halpha6822']

# IO:I example observation with target1
observationIOI = {
    'target': target1,
    'instrument': 'IO:I',  # Single H-band filter instrument
    'exp_time': '120.0',   # Image exposure time for target
    'exp_count': '5',      # Number of target images needed
}


# Sprat example observation with target1
observationSprat = {
    'target': target1,
    'instrument': 'Sprat',
    'exp_time': '120.0',  # Image exposure time for target
    'exp_count': '3',     # Number of target images needed
    'grating': 'blue',    # Grating colour ['blue','red']
}

# FRODOspec example observation with target1
observationFrodo = {
    'target': target1,
    'instrument': 'Frodo',
    'exp_time_Blue': '120.0',  # Image exposure time for blue arm
    'exp_count_Blue': '3',     # Number of exposures for blue arm
    'res_Blue': 'high',        # Blue Spectral Resolution, ['high', 'low']
    'exp_time_Red': '120.0',   # Image exposure time for red arm
    'exp_count_Red': '3',      # Number of exposures for red arm
    'res_Red': 'high',         # Red Spectral Resolution, ['high', 'low']
}

# Create observation object
obs = ltrtml.LTObs(settings)

# Send observations to telescope, getting uid and error back.
# Shown is a group with a single IOO observation.
uid, error = obs.submit_group([observationIOO], constraints)
if error:
    print(error)
else:
    print(uid, ' sucessfully sent to telescope')


# Cancel an observation
error = obs.cancel_group(uid)
if error:
    print(error)
else:
    print('Successfully deleted observation ', uid)

# List current uids which have been submitted to the telescope
print(obs.get_uids())

# Cancel all observations in the proposal that have been sent via ltrtml
for uid in obs.get_uids():
    obs.cancel_group(uid)
