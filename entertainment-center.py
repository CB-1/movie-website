#Submitted by Cheryl J. Banks

import fresh_tomatoes
import media

castaway = media.Movie("Castaway",
						"A man who survives a tragic plane crash struggles to survive alone on a remote island for years.",
						"poster-castaway.png",
						"https://www.youtube.com/watch?v=4tVklCz2jcI")

the_social_network = media.Movie("The Social Network",
						"The story of billionaire Mark Zuckerberg's creation of the global social network known as Facebook.",
						"poster-the-social-network.png",
						"https://www.youtube.com/watch?v=lB95KLmpLR4&t=30s")

threetentoyuma = media.Movie("3:10 to Yuma", 
						"The owner of a distressed ranch accepts a job to escort a captured outlaw to the 3:10 train to Yuma.",
						"poster-310-to-yuma.png",
						"https://www.youtube.com/watch?v=mmtYNhFTPpw&t=21s")
						
heat = media.Movie("Heat",
					"A career criminal and an ambitious detective set out on a dangerous game of cat and mouse.",
					"poster-heat.png",
					"https://www.youtube.com/watch?v=0xbBLJ1WGwQ")

drive = media.Movie("Drive",
					"An experienced Hollywood stuntman moonlights as a getaway driver-for-hire for criminals.",
					"poster-drive.png",
					"https://www.youtube.com/watch?v=KBiOF3y1W0Y")

nocountryforoldmen = media.Movie("No Country for Old Men",
					"Trouble appears when a man finds an abandoned suitcase full of money in the middle of the desert.",
					"poster-nocountryforoldmen.png",
					"https://www.youtube.com/watch?v=A0oNrgumrlE")
					
alien = media.Movie("Alien",
					"An interstellar search-and-rescue mission goes awry when a mysterious creature is discovered.",
					"poster-alien.png",
					"https://www.youtube.com/watch?v=J_5shs8SwEo&t=36s")
					
unforgiven = media.Movie("Unforgiven",
					"A retired gunslinger returns to chase a large bounty posted to kill or capture two renegade outlaws.",
					"poster-unforgiven.png",
					"https://www.youtube.com/watch?v=amE57OniG9Y")
					
i_am_legend = media.Movie("I Am Legend",
					"The lone survivor of a viral outbreak struggles to survive amidst a world of night-stalking creatures.",
					"poster-i-am-legend.png",
					"https://www.youtube.com/watch?v=sFNPNT_4Qww")					

movies = [castaway,the_social_network,threetentoyuma,heat,drive,nocountryforoldmen,alien,unforgiven,iamlegend]
fresh_tomatoes.open_movies_page(movies)

				

