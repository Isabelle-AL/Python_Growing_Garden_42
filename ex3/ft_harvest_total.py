# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isabelle <isabelle@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/06 17:14:51 by iscarval          #+#    #+#              #
#    Updated: 2026/08/09 13:24:14 by isabelle         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
	harvest1 = int(input("Day 1 harvest: "))
	harvest2 = int(input("Day 2 harvest: "))
	harvest3 = int(input("Day 3 harvest: "))
	total = harvest1 + harvest2 + harvest3
	print("Total harvest:", total)
	