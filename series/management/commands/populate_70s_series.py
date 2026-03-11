from django.core.management.base import BaseCommand
from series.models import Series, Season, Episode, Sequence, Shot, Character, WardrobeItem, ShotCharacter
from datetime import timedelta


class Command(BaseCommand):
    help = 'Populate database with 70s TV series data'

    def handle(self, *args, **options):
        self.stdout.write('Creating 70s TV series data...')
        
        # Create The Rockford Files
        self.create_rockford_files()
        
        # Create Starsky & Hutch
        self.create_starsky_hutch()
        
        # Create Kojak
        self.create_kojak()
        
        self.stdout.write(self.style.SUCCESS('Successfully created 70s TV series data!'))

    def create_rockford_files(self):
        self.stdout.write('Creating The Rockford Files...')
        
        # Create Series
        series, _ = Series.objects.get_or_create(
            title="The Rockford Files",
            defaults={
                'description': "Private investigator Jim Rockford solves cases in Los Angeles while living in a trailer in Malibu."
            }
        )
        
        # Create Characters
        jim, _ = Character.objects.get_or_create(name="Jim Rockford")
        jim.series.add(series)
        
        rocky, _ = Character.objects.get_or_create(name="Rocky Rockford")
        rocky.series.add(series)
        
        dennis, _ = Character.objects.get_or_create(name="Dennis Becker")
        dennis.series.add(series)
        
        beth, _ = Character.objects.get_or_create(name="Beth Davenport")
        beth.series.add(series)
        
        # Create Wardrobe
        jim_jacket, _ = WardrobeItem.objects.get_or_create(
            character=jim,
            name="Tan Blazer",
            defaults={'description': 'Signature tan blazer with white shirt'}
        )
        
        # Create Season 1
        season1, _ = Season.objects.get_or_create(
            series=series,
            number=1,
            defaults={'description': 'First season of The Rockford Files'}
        )
        
        # Create Episode 1 - The Kirkoff Case
        ep1, _ = Episode.objects.get_or_create(
            season=season1,
            number=1,
            defaults={
                'title': "The Kirkoff Case",
                'description': "Jim Rockford is hired to investigate the death of a wealthy man's wife.",
                'duration': timedelta(minutes=60),
                'script_author': 'Stephen J. Cannell',
                'script_status': 'final',
                'script': '''
FADE IN:

EXT. MALIBU BEACH - DAY

The Pacific Ocean crashes against the shore. We see a beat-up trailer parked on the beach. This is Jim Rockford's home.

INT. JIM ROCKFORD'S TRAILER - DAY

JIM ROCKFORD (40s) sits at his desk, answering machine playing.

ANSWERING MACHINE (V.O.)
This is Jim Rockford. At the tone, leave your name and message. I'll get back to you.

The machine BEEPS.

LARRY KIRKOFF (V.O.)
Mr. Rockford, this is Larry Kirkoff. I need to see you immediately. My wife has been murdered and the police think I did it.

Jim picks up the phone and dials.

JIM
(into phone)
Mr. Kirkoff, this is Jim Rockford. I got your message.

EXT. KIRKOFF MANSION - DAY

A sprawling estate in Bel Air. Jim's Firebird pulls up.

INT. KIRKOFF MANSION - LIVING ROOM - DAY

LARRY KIRKOFF (50s, wealthy, nervous) paces. Jim enters.

LARRY
Mr. Rockford, thank you for coming. The police are going to arrest me. I didn't kill my wife, but they think I did.

JIM
Why do they think that?

LARRY
Because I was having an affair. Because my wife was worth fifty million dollars. Because...

Jim holds up his hand.

JIM
Slow down. Start from the beginning.

LARRY
My wife, Valerie, was found dead in our pool last night. Drowned. But Valerie was an expert swimmer. She would never drown.

JIM
Unless someone helped her.

LARRY
Exactly. And the police think that someone was me.

Jim pulls out a notebook.

JIM
I'll need access to everything. Bank records, phone logs, your wife's schedule. And I'll need to talk to your girlfriend.

LARRY
(nervous)
How did you know about her?

JIM
(smiles)
I'm a detective, Mr. Kirkoff. It's what I do.

FADE OUT.
                '''
            }
        )
        
        # Create Sequences (Scenes) for Episode 1
        seq1, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=1,
            defaults={
                'title': 'Opening - The Trailer',
                'description': 'Jim in his trailer, answering machine message'
            }
        )
        
        # Create Shots for Sequence 1
        shot1, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=1,
            defaults={
                'script': 'Wide shot of Malibu beach with trailer',
                'camera_angle': 'Wide establishing shot',
                'camera_movement': 'Static, slight zoom in',
                'background': 'Pacific Ocean, beach, blue sky',
                'duration': timedelta(seconds=5)
            }
        )
        
        shot2, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=2,
            defaults={
                'script': 'Medium shot of Jim at desk',
                'camera_angle': 'Medium shot, eye level',
                'camera_movement': 'Static',
                'background': 'Trailer interior, cluttered desk',
                'duration': timedelta(seconds=8)
            }
        )
        shot2.characters.add(jim)
        
        shot3, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=3,
            defaults={
                'script': 'Close-up on answering machine',
                'camera_angle': 'Close-up',
                'camera_movement': 'Static',
                'background': 'Desk with papers',
                'duration': timedelta(seconds=3)
            }
        )
        
        # Sequence 2 - Kirkoff Mansion
        seq2, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=2,
            defaults={
                'title': 'The Kirkoff Mansion',
                'description': 'Jim meets Larry Kirkoff at his mansion'
            }
        )
        
        shot4, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=1,
            defaults={
                'script': 'Wide shot of mansion with Firebird arriving',
                'camera_angle': 'Wide establishing shot, low angle',
                'camera_movement': 'Pan right as car arrives',
                'background': 'Bel Air mansion, palm trees, gate',
                'duration': timedelta(seconds=6)
            }
        )
        
        shot5, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=2,
            defaults={
                'script': 'Two-shot of Jim and Larry talking',
                'camera_angle': 'Medium two-shot',
                'camera_movement': 'Static',
                'background': 'Luxurious living room, fireplace',
                'duration': timedelta(seconds=45)
            }
        )
        shot5.characters.add(jim)
        
        shot6, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=3,
            defaults={
                'script': 'Close-up of Larry looking nervous',
                'camera_angle': 'Close-up, slightly low angle',
                'camera_movement': 'Static',
                'background': 'Blurred living room',
                'duration': timedelta(seconds=12)
            }
        )
        
        # Sequence 3 - Police Station
        seq3, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=3,
            defaults={
                'title': 'Police Station',
                'description': 'Jim visits Detective Becker at the police station'
            }
        )
        
        shot7, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=1,
            defaults={
                'script': 'Wide shot of police station exterior',
                'camera_angle': 'Wide establishing shot',
                'camera_movement': 'Static',
                'background': 'LAPD building, police cars',
                'duration': timedelta(seconds=4)
            }
        )
        
        shot8, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=2,
            defaults={
                'script': 'Over-the-shoulder shot of Jim talking to Dennis',
                'camera_angle': 'OTS, over Dennis shoulder',
                'camera_movement': 'Static',
                'background': 'Police office, cluttered desk, filing cabinets',
                'duration': timedelta(seconds=30)
            }
        )
        shot8.characters.add(jim, dennis)
        
        shot9, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=3,
            defaults={
                'script': 'Reverse OTS of Dennis',
                'camera_angle': 'OTS, over Jim shoulder',
                'camera_movement': 'Static',
                'background': 'Police office',
                'duration': timedelta(seconds=30)
            }
        )
        shot9.characters.add(jim, dennis)
        
        # Link wardrobe to shots
        ShotCharacter.objects.get_or_create(
            shot=shot5,
            character=jim,
            defaults={'wardrobe': jim_jacket}
        )
        
        ShotCharacter.objects.get_or_create(
            shot=shot8,
            character=jim,
            defaults={'wardrobe': jim_jacket}
        )
        
        self.stdout.write('  Created: The Rockford Files - S01E01 The Kirkoff Case')

    def create_starsky_hutch(self):
        self.stdout.write('Creating Starsky & Hutch...')
        
        # Create Series
        series, _ = Series.objects.get_or_create(
            title="Starsky & Hutch",
            defaults={
                'description': "Two streetwise cops bust criminals in their red-and-white Ford Torino in the fictional city of Bay City, California."
            }
        )
        
        # Create Characters
        starsky, _ = Character.objects.get_or_create(name="Dave Starsky")
        starsky.series.add(series)
        
        hutch, _ = Character.objects.get_or_create(name="Ken Hutchinson")
        hutch.series.add(series)
        
        huggy, _ = Character.objects.get_or_create(name="Huggy Bear")
        huggy.series.add(series)
        
        dobbie, _ = Character.objects.get_or_create(name="Captain Dobey")
        dobbie.series.add(series)
        
        # Create Wardrobe
        starsky_sweater, _ = WardrobeItem.objects.get_or_create(
            character=starsky,
            name="Leather Jacket",
            defaults={'description': 'Brown leather jacket with turtleneck sweater'}
        )
        
        hutch_sweater, _ = WardrobeItem.objects.get_or_create(
            character=hutch,
            name="Denim Jacket",
            defaults={'description': 'Blue denim jacket with casual shirt'}
        )
        
        # Create Season 1
        season1, _ = Season.objects.get_or_create(
            series=series,
            number=1,
            defaults={'description': 'First season of Starsky & Hutch'}
        )
        
        # Create Episode 1 - Pilot
        ep1, _ = Episode.objects.get_or_create(
            season=season1,
            number=1,
            defaults={
                'title': "Pilot",
                'description': "Starsky and Hutch investigate a drug ring operating in Bay City.",
                'duration': timedelta(minutes=90),
                'script_author': 'William Blinn',
                'script_status': 'final',
                'script': '''
FADE IN:

EXT. BAY CITY - DAY

The sun rises over the California coast. We see BAY CITY, a sprawling metropolis.

EXT. POLICE HEADQUARTERS - DAY

Two detectives exit the building - DAVE STARSKY and KEN HUTCHINSON.

STARKSY (30s), athletic, wears a leather jacket. HUTCH (30s), blond, more laid-back in denim.

STARKSY
Another beautiful day in paradise, Hutch.

HUTCH
Yeah, right. We got three homicides and a robbery. Some paradise.

They approach a RED AND WHITE FORD TORINO.

INT. TORINO - DAY

They get in. Starsky starts the engine. It ROARS to life.

STARKSY
Let's go see Huggy. He said he had something for us.

EXT. HUGGY BEAR'S - DAY

A flashy bar/restaurant. The Torino pulls up.

INT. HUGGY BEAR'S - DAY

HUGGY BEAR (30s), flamboyant dresser, greets them.

HUGGY
My main men! Starsky and Hutch! What brings you to my humble establishment?

STARKSY
Cut the act, Huggy. You said you had information.

HUGGY
(leaning in, serious)
Word on the street is there's a new player in town. Moving serious weight. Cocaine. Heroin. And he ain't playing nice.

HUTCH
Who is it?

HUGGY
They call him FATS. Big guy. Meaner than a junkyard dog.

Starsky and Hutch exchange looks.

STARKSY
Thanks, Huggy. You know where to find us.

They leave.

EXT. DOCKS - NIGHT

The Torino pulls up near the shipping docks. Starsky and Hutch get out, guns drawn.

STARKSY
(whispering)
You take the left. I'll go right.

They split up, moving through the shadows.

Suddenly, GUNSHOTS RING OUT!

Starsky dives behind a crate. Hutch returns fire.

This is just the beginning...

FADE OUT.
                '''
            }
        )
        
        # Create Sequences for Pilot
        seq1, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=1,
            defaults={
                'title': 'Morning at HQ',
                'description': 'Starsky and Hutch start their day'
            }
        )
        
        shot1, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=1,
            defaults={
                'script': 'Aerial shot of Bay City coastline',
                'camera_angle': 'High angle aerial',
                'camera_movement': 'Helicopter shot, slow pan',
                'background': 'California coast, cityscape, sunrise',
                'duration': timedelta(seconds=8)
            }
        )
        
        shot2, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=2,
            defaults={
                'script': 'Two-shot of Starsky and Hutch exiting building',
                'camera_angle': 'Medium two-shot, eye level',
                'camera_movement': 'Tracking shot as they walk',
                'background': 'Police headquarters, city street',
                'duration': timedelta(seconds=10)
            }
        )
        shot2.characters.add(starsky, hutch)
        
        shot3, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=3,
            defaults={
                'script': 'Low angle shot of Torino',
                'camera_angle': 'Low angle, dramatic',
                'camera_movement': 'Static',
                'background': 'Parking lot, police cars',
                'duration': timedelta(seconds=3)
            }
        )
        
        # Sequence 2 - Huggy Bear's
        seq2, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=2,
            defaults={
                'title': "Huggy Bear's Place",
                'description': 'Getting information from Huggy Bear'
            }
        )
        
        shot4, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=1,
            defaults={
                'script': 'Torino pulling up to Huggy Bear',
                'camera_angle': 'Wide shot',
                'camera_movement': 'Static as car arrives',
                'background': 'Street, Huggy Bear bar exterior',
                'duration': timedelta(seconds=5)
            }
        )
        
        shot5, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=2,
            defaults={
                'script': 'Medium shot of Huggy greeting Starsky and Hutch',
                'camera_angle': 'Medium shot, slight low angle',
                'camera_movement': 'Static',
                'background': 'Bar interior, colorful decor',
                'duration': timedelta(seconds=20)
            }
        )
        shot5.characters.add(starsky, hutch, huggy)
        
        shot6, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=3,
            defaults={
                'script': 'Close-up of Huggy speaking seriously',
                'camera_angle': 'Close-up',
                'camera_movement': 'Slight push in',
                'background': 'Blurred bar interior',
                'duration': timedelta(seconds=15)
            }
        )
        shot6.characters.add(huggy)
        
        # Sequence 3 - Dock Shootout
        seq3, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=3,
            defaults={
                'title': 'Dock Shootout',
                'description': 'Action sequence at the docks'
            }
        )
        
        shot7, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=1,
            defaults={
                'script': 'Wide shot of docks at night',
                'camera_angle': 'Wide establishing shot',
                'camera_movement': 'Slow pan across docks',
                'background': 'Shipping containers, water, moonlight',
                'duration': timedelta(seconds=6)
            }
        )
        
        shot8, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=2,
            defaults={
                'script': 'Starsky and Hutch moving through shadows',
                'camera_angle': 'Medium shot, low angle',
                'camera_movement': 'Tracking shot',
                'background': 'Shadows, shipping containers',
                'duration': timedelta(seconds=12)
            }
        )
        shot8.characters.add(starsky, hutch)
        
        shot9, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=3,
            defaults={
                'script': 'Action shot - Starsky diving behind crate',
                'camera_angle': 'Dynamic medium shot',
                'camera_movement': 'Handheld, shaky',
                'background': 'Docks, crates, dramatic lighting',
                'duration': timedelta(seconds=8)
            }
        )
        shot9.characters.add(starsky)
        
        # Link wardrobe
        ShotCharacter.objects.get_or_create(
            shot=shot2,
            character=starsky,
            defaults={'wardrobe': starsky_sweater}
        )
        ShotCharacter.objects.get_or_create(
            shot=shot2,
            character=hutch,
            defaults={'wardrobe': hutch_sweater}
        )
        
        ShotCharacter.objects.get_or_create(
            shot=shot5,
            character=starsky,
            defaults={'wardrobe': starsky_sweater}
        )
        ShotCharacter.objects.get_or_create(
            shot=shot5,
            character=hutch,
            defaults={'wardrobe': hutch_sweater}
        )
        
        self.stdout.write('  Created: Starsky & Hutch - S01E01 Pilot')

    def create_kojak(self):
        self.stdout.write('Creating Kojak...')
        
        # Create Series
        series, _ = Series.objects.get_or_create(
            title="Kojak",
            defaults={
                'description': "Tough, bald NYPD detective Theo Kojak fights crime in New York City with his trademark lollipops and catchphrase 'Who loves ya, baby?'"
            }
        )
        
        # Create Characters
        kojak, _ = Character.objects.get_or_create(name="Theo Kojak")
        kojak.series.add(series)
        
        crocker, _ = Character.objects.get_or_create(name="Bobby Crocker")
        crocker.series.add(series)
        
        mcneil, _ = Character.objects.get_or_create(name="Captain McNeil")
        mcneil.series.add(series)
        
        # Create Wardrobe
        kojak_suit, _ = WardrobeItem.objects.get_or_create(
            character=kojak,
            name="Brown Three-Piece Suit",
            defaults={'description': 'Signature brown three-piece suit with wide lapels'}
        )
        
        kojak_trench, _ = WardrobeItem.objects.get_or_create(
            character=kojak,
            name="Tan Trench Coat",
            defaults={'description': 'Classic detective trench coat'}
        )
        
        # Create Season 1
        season1, _ = Season.objects.get_or_create(
            series=series,
            number=1,
            defaults={'description': 'First season of Kojak'}
        )
        
        # Create Episode 1 - Siege of Terror
        ep1, _ = Episode.objects.get_or_create(
            season=season1,
            number=1,
            defaults={
                'title': "Siege of Terror",
                'description': "Kojak negotiates with terrorists holding hostages in a hospital.",
                'duration': timedelta(minutes=60),
                'script_author': 'Abby Mann',
                'script_status': 'final',
                'script': '''
FADE IN:

EXT. MANHATTAN - DAY

The New York City skyline. The camera moves down to street level where we see THEO KOJAK (50s), bald, wearing a sharp brown suit, sucking on a lollipop.

INT. MANHATTAN GENERAL HOSPITAL - DAY

A routine day turns chaotic. Two ARMED MEN burst in, firing weapons. They take hostages - doctors, nurses, patients.

HOSTAGE TAKER #1
Nobody moves! This is a revolution!

INT. POLICE COMMAND CENTER - DAY

Kojak stands before a wall of monitors showing the hospital interior. CAPTAIN McNEIL (50s) paces nervously.

McNEIL
Theodore, we need to end this. SWAT is ready to go in.

KOJAK
(holding up hand)
Easy, Frank. We go in there guns blazing, people die. Let me talk to them.

McNEIL
You can't reason with terrorists.

KOJAK
(smiling, lollipop in mouth)
Who says I'm going to reason? I'm going to negotiate. There's a difference.

Kojak picks up the phone and dials.

INT. HOSPITAL LOBBY - DAY

The hostage taker answers the ringing phone.

HOSTAGE TAKER
Yeah?

KOJAK (V.O.)
(filtered)
This is Lieutenant Theo Kojak, NYPD. I want to talk.

HOSTAGE TAKER
We got demands! We want a plane to Cuba! And a million dollars!

INT. COMMAND CENTER - DAY

Kojak chuckles.

KOJAK
(into phone)
A million dollars? What do you think this is, a movie? Listen, let me tell you what's going to happen. You're going to let those people go, and then you and I are going to have a conversation like gentlemen.

HOSTAGE TAKER
Or what?

KOJAK
Or I'm going to come in there and arrest you. And trust me, you don't want that.

The hostage taker is silent. Kojak's confidence is unnerving.

KOJAK (CONT'D)
Who loves ya, baby?

FADE OUT.
                '''
            }
        )
        
        # Create Sequences
        seq1, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=1,
            defaults={
                'title': 'Opening - Manhattan',
                'description': 'Kojak walking through Manhattan streets'
            }
        )
        
        shot1, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=1,
            defaults={
                'script': 'Wide shot of Manhattan skyline',
                'camera_angle': 'Wide establishing shot, high angle',
                'camera_movement': 'Tilt down from skyline to street',
                'background': 'NYC skyline, Empire State Building, busy streets',
                'duration': timedelta(seconds=10)
            }
        )
        
        shot2, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=2,
            defaults={
                'script': 'Medium shot of Kojak walking',
                'camera_angle': 'Medium shot, eye level',
                'camera_movement': 'Tracking shot following Kojak',
                'background': 'Busy Manhattan street, taxis, pedestrians',
                'duration': timedelta(seconds=15)
            }
        )
        shot2.characters.add(kojak)
        
        shot3, _ = Shot.objects.get_or_create(
            sequence=seq1,
            number=3,
            defaults={
                'script': 'Close-up of Kojak with lollipop',
                'camera_angle': 'Close-up',
                'camera_movement': 'Static',
                'background': 'Blurred city background',
                'duration': timedelta(seconds=5)
            }
        )
        shot3.characters.add(kojak)
        
        # Sequence 2 - Hospital Siege
        seq2, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=2,
            defaults={
                'title': 'Hospital Siege Begins',
                'description': 'Terrorists take over the hospital'
            }
        )
        
        shot4, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=1,
            defaults={
                'script': 'Wide shot of hospital lobby',
                'camera_angle': 'Wide shot, high angle',
                'camera_movement': 'Static',
                'background': 'Hospital lobby, people waiting, reception desk',
                'duration': timedelta(seconds=6)
            }
        )
        
        shot5, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=2,
            defaults={
                'script': 'Dynamic shot - terrorists burst in',
                'camera_angle': 'Low angle, dramatic',
                'camera_movement': 'Handheld, chaotic movement',
                'background': 'Hospital entrance, people screaming',
                'duration': timedelta(seconds=10)
            }
        )
        
        shot6, _ = Shot.objects.get_or_create(
            sequence=seq2,
            number=3,
            defaults={
                'script': 'Close-up of hostage taker shouting',
                'camera_angle': 'Close-up, intense',
                'camera_movement': 'Slight handheld shake',
                'background': 'Blurred hospital interior, panic',
                'duration': timedelta(seconds=8)
            }
        )
        
        # Sequence 3 - Command Center
        seq3, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=3,
            defaults={
                'title': 'Police Command Center',
                'description': 'Kojak takes charge at the command center'
            }
        )
        
        shot7, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=1,
            defaults={
                'script': 'Wide shot of command center with monitors',
                'camera_angle': 'Wide establishing shot',
                'camera_movement': 'Pan across room',
                'background': 'Police command center, monitors, officers',
                'duration': timedelta(seconds=8)
            }
        )
        
        shot8, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=2,
            defaults={
                'script': 'Two-shot of Kojak and McNeil',
                'camera_angle': 'Medium two-shot',
                'camera_movement': 'Static',
                'background': 'Command center, wall of monitors',
                'duration': timedelta(seconds=25)
            }
        )
        shot8.characters.add(kojak, mcneil)
        
        shot9, _ = Shot.objects.get_or_create(
            sequence=seq3,
            number=3,
            defaults={
                'script': 'Close-up of Kojak on phone',
                'camera_angle': 'Close-up, intense',
                'camera_movement': 'Slow push in',
                'background': 'Command center, blurred',
                'duration': timedelta(seconds=20)
            }
        )
        shot9.characters.add(kojak)
        
        # Sequence 4 - Crocker Arrives
        seq4, _ = Sequence.objects.get_or_create(
            episode=ep1,
            number=4,
            defaults={
                'title': "Crocker's Arrival",
                'description': 'Detective Crocker joins Kojak'
            }
        )
        
        shot10, _ = Shot.objects.get_or_create(
            sequence=seq4,
            number=1,
            defaults={
                'script': 'Medium shot of Crocker entering',
                'camera_angle': 'Medium shot, doorway frame',
                'camera_movement': 'Static',
                'background': 'Command center entrance',
                'duration': timedelta(seconds=5)
            }
        )
        shot10.characters.add(crocker)
        
        shot11, _ = Shot.objects.get_or_create(
            sequence=seq4,
            number=2,
            defaults={
                'script': 'Three-shot of Kojak, Crocker, and McNeil',
                'camera_angle': 'Medium three-shot',
                'camera_movement': 'Static',
                'background': 'Command center, monitors',
                'duration': timedelta(seconds=30)
            }
        )
        shot11.characters.add(kojak, crocker, mcneil)
        
        # Link wardrobe
        ShotCharacter.objects.get_or_create(
            shot=shot2,
            character=kojak,
            defaults={'wardrobe': kojak_suit}
        )
        
        ShotCharacter.objects.get_or_create(
            shot=shot8,
            character=kojak,
            defaults={'wardrobe': kojak_trench}
        )
        
        ShotCharacter.objects.get_or_create(
            shot=shot9,
            character=kojak,
            defaults={'wardrobe': kojak_trench}
        )
        
        ShotCharacter.objects.get_or_create(
            shot=shot11,
            character=kojak,
            defaults={'wardrobe': kojak_trench}
        )
        
        self.stdout.write('  Created: Kojak - S01E01 Siege of Terror')
