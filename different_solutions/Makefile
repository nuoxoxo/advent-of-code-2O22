#comp	:=	c++ -std=c++11 -Wall -Werror -Wextra
comp	:=	c++ -std=c++11 
name	:=	out
rmv	:=	rm -f
src	:=	test_parsing.cc
src	:=	aoc2222_initial_submit_p1.cc
src	:=	aoc2222_initial_submit_p2.cc

all	:	$(name)

$(name)	:	$(src)
		@ $(comp) $^ -o $@
		@ echo "data" && echo "" 
		@ ./$(name) < ../_inputs/2222.0
		@ echo "" && echo "test" && echo ""
		@ ./$(name) < ../_inputs/2222.1
		@ make f

clean	:
		@ $(rmv) $(name)

fclean	:	clean
		@ $(rmv) out *.out

f	:	fclean
re	:	f all
.PHONY	:	fclean clean all re f

