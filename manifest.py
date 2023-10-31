# aircraft_manifest.py
import json

class AircraftManifest:
    def __init__(self, manifest_data):
        self.manifest = manifest_data

    def get_passenger_manifest(self):
        passenger_manifest = sorted(
            filter(lambda passenger: passenger[1] and passenger[2], self.manifest),
            key=lambda passenger: (passenger[2].lower(), passenger[1].lower())
        )
        return passenger_manifest

    def purchase_ticket(self, first_name, last_name, seat):
        seat = seat.upper()
        for passenger in self.manifest:
            if passenger[0].upper() == seat and passenger[1] and passenger[2]:
                return False
        for passenger in self.manifest:
            if passenger[0].upper() == seat:
                passenger[1] = first_name
                passenger[2] = last_name
                return True
        return False

    def cancel_ticket(self, seat):
        seat = seat.upper()
        for passenger in self.manifest:
            if passenger[0].upper() == seat and not passenger[1] and not passenger[2]:
                return False
        for passenger in self.manifest:
            if passenger[0].upper() == seat:
                passenger[1] = ''
                passenger[2] = ''
                passenger[3] = False
                passenger[4] = 0
                passenger[5] = False
                return True

    def check_in(self, seat):
        seat = seat.upper()
        for passenger in self.manifest:
            if passenger[0].upper() == seat and not passenger[1] and not passenger[2]:
                return False
        for passenger in self.manifest:
            if passenger[0].upper() == seat:
                passenger[3] = True
                return True

    def check_bags(self, seat, no_bags):
        seat = seat.upper()
        for passenger in self.manifest:
            if passenger[0].upper() == seat and not passenger[1] and not passenger[2]:
                return False
            if passenger[0].upper() == seat and not passenger[3]:
                return False
        for passenger in self.manifest:
            if passenger[0].upper() == seat:
                passenger[4] = no_bags
                return True

    def board_aircraft(self, seat):
        seat = seat.upper()
        for passenger in self.manifest:
            if passenger[0].upper() == seat and not passenger[1] and not passenger[2]:
                return False
            if passenger[0].upper() == seat and not passenger[3]:
                return False
        for passenger in self.manifest:
            if passenger[0].upper() == seat:
                passenger[5] = True
                return True

    def save_to_json(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.manifest, file)

    @classmethod
    def load_from_json(cls, filename):
        with open(filename, 'r') as file:
            manifest_data = json.load(file)
            return cls(manifest_data)
