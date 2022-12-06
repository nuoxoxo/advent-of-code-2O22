#comp	:=	c++ -std=c++11 -Wall -Werror -Wextra
comp	:=	c++ -std=c++11 
name	:=	out
rmv	:=	rm -f

src	:=	aoc2201.cc
src	:=	aoc2202a.cc
src	:=	aoc2202.cc
src	:=	aoc2203a.cc
src	:=	aoc2203.cc
src	:=	aoc2204a.cc
src	:=	aoc2204.cc
src	:=	aoc2205a.cc
src	:=	aoc2205.cc
src	:=	aoc2205_part1.cc
src	:=	aoc2205_part2.cc
src	:=	aoc2206.cc

all	:	$(name)

$(name)	:	$(src)
		@ $(comp) $^ -o $@
		@ echo "data" && echo "" 
		@ ./$(name) < 2206.0
		@#@ ./$(name) < 2205.0
		@#@ ./$(name) < 2204.0
		@#@ ./$(name) < 2204a.0
		@#@ ./$(name) < 2203.0
		@#@ ./$(name) < 2203a.0
		@#@ ./$(name) < 2202.0
		@#@ ./$(name) < 2202a.0
		@#@ ./$(name) < 2201.0
		@ echo "" && echo "test" && echo ""
		@ ./$(name) < test
		@ make f

clean	:
		@ $(rmv) $(name)

fclean	:	clean
		@ $(rmv) out *.out

f	:	fclean
re	:	f all
.PHONY	:	fclean clean all re f
