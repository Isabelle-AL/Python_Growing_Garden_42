# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: isabelle <isabelle@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/09 19:05:39 by isabelle          #+#    #+#              #
#    Updated: 2026/08/09 19:49:05 by isabelle         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if unit == "packets":
		print(seed_type.capitalize(), "seeds:", quantity, unit, "available")
	elif unit == "grams":
		print(seed_type.capitalize(), "seeds:", quantity, unit, "total")
	elif unit == "area":
		print(seed_type.capitalize(), "seeds:", "covers", quantity, "square meters")
	else:
		print("Unknown unit type")
