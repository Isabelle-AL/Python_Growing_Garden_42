# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isabelle <isabelle@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/06 20:52:32 by iscarval          #+#    #+#              #
#    Updated: 2026/08/09 13:24:02 by isabelle         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
	days = int(input("Days until harvest: "))
	for i in range(1, days + 1):
		print("Day", i)
	print("Harvest time!")
