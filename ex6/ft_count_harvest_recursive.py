# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isabelle <isabelle@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/09 11:35:26 by isabelle          #+#    #+#              #
#    Updated: 2026/08/09 19:15:24 by isabelle         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	count_day(1, days)

def count_day(day, days):
	if day <= days:
		print("Day", day)
		count_day(day + 1, days)
	else:
		print("Harvest time!")
