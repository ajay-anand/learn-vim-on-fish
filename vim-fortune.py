ROM = """|i_CTRL-@|	CTRL-@		insert previously inserted text and stop insert
|i_CTRL-A|	CTRL-A		insert previously inserted text
|i_CTRL-C|	CTRL-C		quit insert mode, without checking for abbreviation
|i_CTRL-D|	CTRL-D		delete one shiftwidth of indent in the current line
|i_CTRL-E|	CTRL-E		insert the character which is below the cursor
|i_CTRL-G_j|	CTRL-G CTRL-J	line down, to column where inserting started
|i_CTRL-G_j|	CTRL-G j	line down, to column where inserting started
|i_CTRL-G_j|	CTRL-G <Down>	line down, to column where inserting started
|i_CTRL-G_k|	CTRL-G CTRL-K	line up, to column where inserting started
|i_CTRL-G_k|	CTRL-G k	line up, to column where inserting started
|i_CTRL-G_k|	CTRL-G <Up>	line up, to column where inserting started
|i_CTRL-G_u|	CTRL-G u	start new undoable edit
|i_CTRL-G_U|	CTRL-G U	don't break undo with next cursor movement
|i_<BS>|	<BS>		delete character before the cursor
|i_digraph|	{char1}<BS>{char2} enter digraph (only when 'digraph' option set)
|i_CTRL-H|	CTRL-H		same as <BS>
|i_<Tab>|	<Tab>		insert a <Tab> character
|i_CTRL-I|	CTRL-I		same as <Tab>
|i_<NL>|	<NL>		same as <CR>
|i_CTRL-J|	CTRL-J		same as <CR>
|i_CTRL-K|	CTRL-K {char1} {char2} enter digraph
|i_<CR>|	<CR>		begin new line
|i_CTRL-M|	CTRL-M		same as <CR>
|i_CTRL-N|	CTRL-N		find next match for keyword in front of the cursor
|i_CTRL-O|	CTRL-O		execute a single command and return to insert mode
|i_CTRL-P|	CTRL-P		find previous match for keyword in front of the cursor
|i_CTRL-Q|	CTRL-Q		same as CTRL-V, unless used for terminal control flow
|i_CTRL-SHIFT-Q|  CTRL-SHIFT-Q {char} like CTRL-Q unless |tui-modifyOtherKeys| is active
|i_CTRL-R|	CTRL-R {register} insert the contents of a register
|i_CTRL-R_CTRL-R| CTRL-R CTRL-R {register} insert the contents of a register literally
|i_CTRL-R_CTRL-O| CTRL-R CTRL-O {register} insert the contents of a register literally and don't auto-indent
|i_CTRL-R_CTRL-P| CTRL-R CTRL-P {register} insert the contents of a register literally and fix indent.
|i_CTRL-T|	CTRL-T		insert one shiftwidth of indent in current line
|i_CTRL-U|	CTRL-U		delete all entered characters in the current line
|i_CTRL-V|	CTRL-V {char}	insert next non-digit literally
|i_CTRL-SHIFT-V|  CTRL-SHIFT-V {char} like CTRL-V unless |tui-modifyOtherKeys| is active
|i_CTRL-V_digit| CTRL-V {number} insert three digit decimal number as a single byte.
|i_CTRL-W|	CTRL-W		delete word before the cursor
|i_CTRL-X|	CTRL-X {mode}	enter CTRL-X sub mode, see |i_CTRL-X_index|
|i_CTRL-Y|	CTRL-Y		insert the character which is above the cursor
|i_<Esc>|	<Esc>		end insert mode
|i_CTRL-[|	CTRL-[		same as <Esc>
|i_CTRL-\_CTRL-N| CTRL-\ CTRL-N	go to Normal mode
|i_CTRL-\_CTRL-G| CTRL-\ CTRL-G	go to Normal mode
|i_CTRL-]|	CTRL-]		trigger abbreviation
|i_CTRL-^|	CTRL-^		toggle use of |:lmap| mappings
|i_CTRL-_|	CTRL-_		When 'allowrevins' set: change language (Hebrew)
|i_0_CTRL-D|	0 CTRL-D	delete all indent in the current line
|i_^_CTRL-D|	^ CTRL-D	delete all indent in the current line, restore it in the next line
|i_<Del>|	<Del>		delete character under the cursor
|i_<Left>|	<Left>		cursor one character left
|i_<S-Left>|	<S-Left>	cursor one word left
|i_<C-Left>|	<C-Left>	cursor one word left
|i_<Right>|	<Right>		cursor one character right
|i_<S-Right>|	<S-Right>	cursor one word right
|i_<C-Right>|	<C-Right>	cursor one word right
|i_<Up>|	<Up>		cursor one line up
|i_<S-Up>|	<S-Up>		same as <PageUp>
|i_<Down>|	<Down>		cursor one line down
|i_<S-Down>|	<S-Down>	same as <PageDown>
|i_<Home>|	<Home>		cursor to start of line
|i_<C-Home>|	<C-Home>	cursor to start of file
|i_<End>|	<End>		cursor past end of line
|i_<C-End>|	<C-End>		cursor past end of file
|i_<PageUp>|	<PageUp>	one screenful backward
|i_<PageDown>|	<PageDown>	one screenful forward
|i_<F1>|	<F1>		same as <Help>
|i_<Help>|	<Help>		stop insert mode and display help window
|i_<Insert>|	<Insert>	toggle Insert/Replace mode
|i_CTRL-X_CTRL-D|	CTRL-X CTRL-D	complete defined identifiers
|i_CTRL-X_CTRL-E|	CTRL-X CTRL-E	scroll up
|i_CTRL-X_CTRL-F|	CTRL-X CTRL-F	complete file names
|i_CTRL-X_CTRL-I|	CTRL-X CTRL-I	complete identifiers
|i_CTRL-X_CTRL-K|	CTRL-X CTRL-K	complete identifiers from dictionary
|i_CTRL-X_CTRL-L|	CTRL-X CTRL-L	complete whole lines
|i_CTRL-X_CTRL-N|	CTRL-X CTRL-N	next completion
|i_CTRL-X_CTRL-O|	CTRL-X CTRL-O	omni completion
|i_CTRL-X_CTRL-P|	CTRL-X CTRL-P	previous completion
|i_CTRL-X_CTRL-S|	CTRL-X CTRL-S	spelling suggestions
|i_CTRL-X_CTRL-T|	CTRL-X CTRL-T	complete identifiers from thesaurus
|i_CTRL-X_CTRL-Y|	CTRL-X CTRL-Y	scroll down
|i_CTRL-X_CTRL-U|	CTRL-X CTRL-U	complete with 'completefunc'
|i_CTRL-X_CTRL-V|	CTRL-X CTRL-V	complete like in : command line
|i_CTRL-X_CTRL-Z|	CTRL-X CTRL-Z	stop completion, keeping the text as-is
|i_CTRL-X_CTRL-]|	CTRL-X CTRL-]	complete tags
|i_CTRL-X_s|		CTRL-X s	spelling suggestions
|complete_CTRL-E| CTRL-E	stop completion and go back to original text
|complete_CTRL-Y| CTRL-Y	accept selected match and stop completion
complete		CTRL-L		insert one character from the current match
complete		<CR>		insert currently selected match
complete		<BS>		delete one character and redo search
complete		CTRL-H		same as <BS>
complete		<Up>		select the previous match
complete		<Down>		select the next match
complete		<PageUp>	select a match several entries back
complete		<PageDown>	select a match several entries forward
|CTRL-A|	CTRL-A		2  add N to number at/after cursor
|CTRL-B|	CTRL-B		1  scroll N screens Backwards
|CTRL-C|	CTRL-C		   interrupt current (search) command
|CTRL-D|	CTRL-D		   scroll Down N lines (default: half a screen)
|CTRL-E|	CTRL-E		   scroll N lines upwards (N lines Extra)
|CTRL-F|	CTRL-F		1  scroll N screens Forward
|CTRL-G|	CTRL-G		   display current file name and position
|<BS>|		<BS>		1  same as "h"
|CTRL-H|	CTRL-H		1  same as "h"
|<Tab>|		<Tab>		1  go to N newer entry in jump list
|CTRL-I|	CTRL-I		1  same as <Tab>
|<NL>|		<NL>		1  same as "j"
|CTRL-J|	CTRL-J		1  same as "j"
|CTRL-L|	CTRL-L		   redraw screen
|<CR>|		<CR>		1  cursor to the first CHAR N lines lower
|CTRL-M|	CTRL-M		1  same as <CR>
|CTRL-N|	CTRL-N		1  same as "j"
|CTRL-O|	CTRL-O		1  go to N older entry in jump list
|CTRL-P|	CTRL-P		1  same as "k"
|CTRL-R|	CTRL-R		2  redo changes which were undone with 'u'
|CTRL-T|	CTRL-T		   jump to N older Tag in tag list
|CTRL-U|	CTRL-U		   scroll N lines Upwards (default: half a screen)
|CTRL-V|	CTRL-V		   start blockwise Visual mode
|CTRL-W|	CTRL-W {char}	   window commands, see |CTRL-W|
|CTRL-X|	CTRL-X		2  subtract N from number at/after cursor
|CTRL-Y|	CTRL-Y		   scroll N lines downwards
|CTRL-Z|	CTRL-Z		   suspend program (or start new shell)
|CTRL-\_CTRL-N|	CTRL-\ CTRL-N	   go to Normal mode (no-op)
|CTRL-\_CTRL-G|	CTRL-\ CTRL-G	   go to Normal mode (no-op)
|CTRL-]|	CTRL-]		   :ta to ident under cursor
|CTRL-^|	CTRL-^		   edit Nth alternate file (equivalent to ":e #N")
|CTRL-<Tab>|	CTRL-<Tab>	   same as `g<Tab>` : go to last accessed tab page
|<Space>|	<Space>		1  same as "l"
|!|		!{motion}{filter} 2  filter Nmove text through the {filter} command
|!!|		!!{filter}	2  filter N lines through the {filter} command
|quote|		"{register}	   use {register} for next delete, yank or put ({.%#:} only work with put)
|#|		#		1  search backward for the Nth occurrence of the ident under the cursor
|$|		$		1  cursor to the end of Nth next line
|%|		%		1  find the next (curly/square) bracket on this line and go to its match, or go to matching comment bracket, or go to matching preprocessor directive.
|N%|		{count}%	1  go to N percentage in the file
|&|		&		2  repeat last :s
|'|		'{a-zA-Z0-9}	1  cursor to the first CHAR on the line with mark {a-zA-Z0-9}
|''|		''		1  cursor to the first CHAR of the line where the cursor was before the latest jump.
|'(|		'(		1  cursor to the first CHAR on the line of the start of the current sentence
|')|		')		1  cursor to the first CHAR on the line of the end of the current sentence
|'<|		'<		1  cursor to the first CHAR of the line where highlighted area starts/started in the current buffer.
|'>|		'>		1  cursor to the first CHAR of the line where highlighted area ends/ended in the current buffer.
|'[|		'[		1  cursor to the first CHAR on the line of the start of last operated text or start of put text
|']|		']		1  cursor to the first CHAR on the line of the end of last operated text or end of put text
|'{|		'{		1  cursor to the first CHAR on the line of the start of the current paragraph
|'}|		'}		1  cursor to the first CHAR on the line of the end of the current paragraph
|(|		(		1  cursor N sentences backward
|)|		)		1  cursor N sentences forward
|star|		*		1  search forward for the Nth occurrence of the ident under the cursor
|+|		+		1  same as <CR>
|,|		,		1  repeat latest f, t, F or T in opposite direction N times
|-|		-		1  cursor to the first CHAR N lines higher
|.|		.		2  repeat last change with count replaced with N
|/|		/{pattern}<CR>	1  search forward for the Nth occurrence of {pattern}
|/<CR>|		/<CR>		1  search forward for {pattern} of last search
|0|		0		1  cursor to the first char of the line
|:|		:		1  start entering an Ex command
|N:|		{count}:	   start entering an Ex command with range from current line to N-1 lines down
|;|		;		1  repeat latest f, t, F or T N times
|<|		<{motion}	2  shift Nmove lines one 'shiftwidth' leftwards
|<<|		<<		2  shift N lines one 'shiftwidth' leftwards
|=|		={motion}	2  filter Nmove lines through "indent"
|==|		==		2  filter N lines through "indent"
|>|		>{motion}	2  shift Nmove lines one 'shiftwidth' rightwards
|>>|		>>		2  shift N lines one 'shiftwidth' rightwards
|?|		?{pattern}<CR>	1  search backward for the Nth previous occurrence of {pattern}
|?<CR>|		?<CR>		1  search backward for {pattern} of last search
|@|		@{a-z}		2  execute the contents of register {a-z} N times
|@:|		@:		   repeat the previous ":" command N times
|@@|		@@		2  repeat the previous @{a-z} N times
|A|		A		2  append text after the end of the line N times
|B|		B		1  cursor N WORDS backward
|C|		["x]C		2  change from the cursor position to the end of the line, and N-1 more lines [into register x]; synonym for "c$"
|D|		["x]D		2  delete the characters under the cursor until the end of the line and N-1 more lines [into register x]; synonym for "d$"
|E|		E		1  cursor forward to the end of WORD N
|F|		F{char}		1  cursor to the Nth occurrence of {char} to the left
|G|		G		1  cursor to line N, default last line
|H|		H		1  cursor to line N from top of screen
|I|		I		2  insert text before the first CHAR on the line N times
|J|		J		2  Join N lines; default is 2
|K|		K		   lookup Keyword under the cursor with 'keywordprg'
|L|		L		1  cursor to line N from bottom of screen
|M|		M		1  cursor to middle line of screen
|N|		N		1  repeat the latest '/' or '?' N times in opposite direction
|O|		O		2  begin a new line above the cursor and insert text, repeat N times
|P|		["x]P		2  put the text [from register x] before the cursor N times
|R|		R		2  enter replace mode: overtype existing characters, repeat the entered text N-1 times
|S|		["x]S		2  delete N lines [into register x] and start insert; synonym for "cc".
|T|		T{char}		1  cursor till after Nth occurrence of {char} to the left
|U|		U		2  undo all latest changes on one line
|V|		V		   start linewise Visual mode
|W|		W		1  cursor N WORDS forward
|X|		["x]X		2  delete N characters before the cursor [into register x]
|Y|		["x]Y		   yank N lines [into register x]; synonym for "yy"
|ZZ|		ZZ		   write if buffer changed and close window
|ZQ|		ZQ		   close window without writing
|[|		[{char}		   square bracket command (see |[| below)
|]|		]{char}		   square bracket command (see |]| below)
|^|		^		1  cursor to the first CHAR of the line
|_|		_		1  cursor to the first CHAR N - 1 lines lower
|`|		`{a-zA-Z0-9}	1  cursor to the mark {a-zA-Z0-9}
|`(|		`(		1  cursor to the start of the current sentence
|`)|		`)		1  cursor to the end of the current sentence
|`<|		`<		1  cursor to the start of the highlighted area
|`>|		`>		1  cursor to the end of the highlighted area
|`[|		`[		1  cursor to the start of last operated text or start of putted text
|`]|		`]		1  cursor to the end of last operated text or end of putted text
|``|		``		1  cursor to the position before latest jump
|`{|		`{		1  cursor to the start of the current paragraph
|`}|		`}		1  cursor to the end of the current paragraph
|a|		a		2  append text after the cursor N times
|b|		b		1  cursor N words backward
|c|		["x]c{motion}	2  delete Nmove text [into register x] and start insert
|cc|		["x]cc		2  delete N lines [into register x] and start insert
|d|		["x]d{motion}	2  delete Nmove text [into register x]
|dd|		["x]dd		2  delete N lines [into register x]
|do|		do		2  same as ":diffget"
|dp|		dp		2  same as ":diffput"
|e|		e		1  cursor forward to the end of word N
|f|		f{char}		1  cursor to Nth occurrence of {char} to the right
|g|		g{char}		   extended commands, see |g| below
|h|		h		1  cursor N chars to the left
|i|		i		2  insert text before the cursor N times
|j|		j		1  cursor N lines downward
|k|		k		1  cursor N lines upward
|l|		l		1  cursor N chars to the right
|m|		m{A-Za-z}	   set mark {A-Za-z} at cursor position
|n|		n		1  repeat the latest '/' or '?' N times
|o|		o		2  begin a new line below the cursor and insert text, repeat N times
|p|		["x]p		2  put the text [from register x] after the cursor N times
|q|		q{0-9a-zA-Z"}	   record typed characters into named register {0-9a-zA-Z"} (uppercase to append)
|q|		q		   (while recording) stops recording
|Q|		Q		   replay last recorded macro
|q:|		q:		   edit : command-line in command-line window
|q/|		q/		   edit / command-line in command-line window
|q?|		q?		   edit ? command-line in command-line window
|r|		r{char}		2  replace N chars with {char}
|s|		["x]s		2  (substitute) delete N characters [into register x] and start insert
|t|		t{char}		1  cursor till before Nth occurrence of {char} to the right
|u|		u		2  undo changes
|v|		v		   start charwise Visual mode
|w|		w		1  cursor N words forward
|x|		["x]x		2  delete N characters under and after the cursor [into register x]
|y|		["x]y{motion}	   yank Nmove text [into register x]
|yy|		["x]yy		   yank N lines [into register x]
|z|		z{char}		   commands starting with 'z', see |z| below
|{|		{		1  cursor N paragraphs backward
|bar|		|		1  cursor to column N
|}|		}		1  cursor N paragraphs forward
|~|		~		2  'tildeop' off: switch case of N characters under cursor and move the cursor N characters to the right
|~|		~{motion}	   'tildeop' on: switch case of Nmove text
|<C-End>|	<C-End>		1  same as "G"
|<C-Home>|	<C-Home>	1  same as "gg"
|<C-Left>|	<C-Left>	1  same as "b"
|<C-Right>|	<C-Right>	1  same as "w"
|<C-Tab>|	<C-Tab>		   same as "g<Tab>"
|<Del>|		["x]<Del>	2  same as "x"
|N<Del>|	{count}<Del>	   remove the last digit from {count}
|<Down>|	<Down>		1  same as "j"
|<End>|		<End>		1  same as "$"
|<F1>|		<F1>		   same as <Help>
|<Help>|	<Help>		   open a help window
|<Home>|	<Home>		1  same as "0"
|<Insert>|	<Insert>	2  same as "i"
|<Left>|	<Left>		1  same as "h"
|<PageDown>|	<PageDown>	   same as CTRL-F
|<PageUp>|	<PageUp>	   same as CTRL-B
|<Right>|	<Right>		1  same as "l"
|<S-Down>|	<S-Down>	1  same as CTRL-F
|<S-Left>|	<S-Left>	1  same as "b"
|<S-Right>|	<S-Right>	1  same as "w"
|<S-Up>|	<S-Up>		1  same as CTRL-B
|<Undo>|	<Undo>		2  same as "u"
|<Up>|		<Up>		1  same as "k"
|v_aquote|	a"		   double quoted string
|v_a'|		a'		   single quoted string
|v_a(|		a(		   same as ab
|v_a)|		a)		   same as ab
|v_a<|		a<		   "a <>" from '<' to the matching '>'
|v_a>|		a>		   same as a<
|v_aB|		aB		   "a Block" from "[{" to "]}" (with brackets)
|v_aW|		aW		   "a WORD" (with white space)
|v_a[|		a[		   "a []" from '[' to the matching ']'
|v_a]|		a]		   same as a[
|v_a`|		a`		   string in backticks
|v_ab|		ab		   "a block" from "[(" to "])" (with braces)
|v_ap|		ap		   "a paragraph" (with white space)
|v_as|		as		   "a sentence" (with white space)
|v_at|		at		   "a tag block" (with white space)
|v_aw|		aw		   "a word" (with white space)
|v_a{|		a{		   same as aB
|v_a}|		a}		   same as aB
|v_iquote|	i"		   double quoted string without the quotes
|v_i'|		i'		   single quoted string without the quotes
|v_i(|		i(		   same as ib
|v_i)|		i)		   same as ib
|v_i<|		i<		   "inner <>" from '<' to the matching '>'
|v_i>|		i>		   same as i<
|v_iB|		iB		   "inner Block" from "[{" and "]}"
|v_iW|		iW		   "inner WORD"
|v_i[|		i[		   "inner []" from '[' to the matching ']'
|v_i]|		i]		   same as i[
|v_i`|		i`		   string in backticks without the backticks
|v_ib|		ib		   "inner block" from "[(" to "])"
|v_ip|		ip		   "inner paragraph"
|v_is|		is		   "inner sentence"
|v_it|		it		   "inner tag block"
|v_iw|		iw		   "inner word"
|v_i{|		i{		   same as iB
|v_i}|		i}		   same as iB
|CTRL-W_CTRL-B|	CTRL-W CTRL-B	   same as "CTRL-W b"
|CTRL-W_CTRL-C|	CTRL-W CTRL-C	   same as "CTRL-W c"
|CTRL-W_CTRL-D|	CTRL-W CTRL-D	   same as "CTRL-W d"
|CTRL-W_CTRL-F|	CTRL-W CTRL-F	   same as "CTRL-W f"
CTRL-W CTRL-G	   same as "CTRL-W g .."
|CTRL-W_CTRL-H|	CTRL-W CTRL-H	   same as "CTRL-W h"
|CTRL-W_CTRL-I|	CTRL-W CTRL-I	   same as "CTRL-W i"
|CTRL-W_CTRL-J|	CTRL-W CTRL-J	   same as "CTRL-W j"
|CTRL-W_CTRL-K|	CTRL-W CTRL-K	   same as "CTRL-W k"
|CTRL-W_CTRL-L|	CTRL-W CTRL-L	   same as "CTRL-W l"
|CTRL-W_CTRL-N|	CTRL-W CTRL-N	   same as "CTRL-W n"
|CTRL-W_CTRL-O|	CTRL-W CTRL-O	   same as "CTRL-W o"
|CTRL-W_CTRL-P|	CTRL-W CTRL-P	   same as "CTRL-W p"
|CTRL-W_CTRL-Q|	CTRL-W CTRL-Q	   same as "CTRL-W q"
|CTRL-W_CTRL-R|	CTRL-W CTRL-R	   same as "CTRL-W r"
|CTRL-W_CTRL-S|	CTRL-W CTRL-S	   same as "CTRL-W s"
|CTRL-W_CTRL-T|	CTRL-W CTRL-T	   same as "CTRL-W t"
|CTRL-W_CTRL-V|	CTRL-W CTRL-V	   same as "CTRL-W v"
|CTRL-W_CTRL-W|	CTRL-W CTRL-W	   same as "CTRL-W w"
|CTRL-W_CTRL-X|	CTRL-W CTRL-X	   same as "CTRL-W x"
|CTRL-W_CTRL-Z|	CTRL-W CTRL-Z	   same as "CTRL-W z"
|CTRL-W_CTRL-]|	CTRL-W CTRL-]	   same as "CTRL-W ]"
|CTRL-W_CTRL-^|	CTRL-W CTRL-^	   same as "CTRL-W ^"
|CTRL-W_CTRL-_|	CTRL-W CTRL-_	   same as "CTRL-W _"
|CTRL-W_+|	CTRL-W +	   increase current window height N lines
|CTRL-W_-|	CTRL-W -	   decrease current window height N lines
|CTRL-W_<|	CTRL-W <	   decrease current window width N columns
|CTRL-W_=|	CTRL-W =	   make all windows the same height & width
|CTRL-W_>|	CTRL-W >	   increase current window width N columns
|CTRL-W_H|	CTRL-W H	   move current window to the far left
|CTRL-W_J|	CTRL-W J	   move current window to the very bottom
|CTRL-W_K|	CTRL-W K	   move current window to the very top
|CTRL-W_L|	CTRL-W L	   move current window to the far right
|CTRL-W_P|	CTRL-W P	   go to preview window
|CTRL-W_R|	CTRL-W R	   rotate windows upwards N times
|CTRL-W_S|	CTRL-W S	   same as "CTRL-W s"
|CTRL-W_T|	CTRL-W T	   move current window to a new tab page
|CTRL-W_W|	CTRL-W W	   go to N previous window (wrap around)
|CTRL-W_]|	CTRL-W ]	   split window and jump to tag under cursor
|CTRL-W_^|	CTRL-W ^	   split current window and edit alternate file N
|CTRL-W__|	CTRL-W _	   set current window height to N (default: very high)
|CTRL-W_b|	CTRL-W b	   go to bottom window
|CTRL-W_c|	CTRL-W c	   close current window (like |:close|)
|CTRL-W_d|	CTRL-W d	   split window and jump to definition under the cursor
|CTRL-W_f|	CTRL-W f	   split window and edit file name under the cursor
|CTRL-W_F|	CTRL-W F	   split window and edit file name under the cursor and jump to the line number following the file name.
|CTRL-W_g_CTRL-]| CTRL-W g CTRL-]  split window and do |:tjump| to tag under cursor
|CTRL-W_g]|	CTRL-W g ]	   split window and do |:tselect| for tag under cursor
|CTRL-W_g}|	CTRL-W g }	   do a |:ptjump| to the tag under the cursor
|CTRL-W_gf|	CTRL-W g f	   edit file name under the cursor in a new tab page
|CTRL-W_gF|	CTRL-W g F	   edit file name under the cursor in a new tab page and jump to the line number following the file name.
|CTRL-W_gt|	CTRL-W g t	   same as `gt`: go to next tab page
|CTRL-W_gT|	CTRL-W g T	   same as `gT`: go to previous tab page
|CTRL-W_g<Tab>|	CTRL-W g <Tab>	   same as |g<Tab>|: go to last accessed tab page
|CTRL-W_h|	CTRL-W h	   go to Nth left window (stop at first window)
|CTRL-W_i|	CTRL-W i	   split window and jump to declaration of identifier under the cursor
|CTRL-W_j|	CTRL-W j	   go N windows down (stop at last window)
|CTRL-W_k|	CTRL-W k	   go N windows up (stop at first window)
|CTRL-W_l|	CTRL-W l	   go to Nth right window (stop at last window)
|CTRL-W_n|	CTRL-W n	   open new window, N lines high
|CTRL-W_o|	CTRL-W o	   close all but current window (like |:only|)
|CTRL-W_p|	CTRL-W p	   go to previous (last accessed) window
|CTRL-W_q|	CTRL-W q	   quit current window (like |:quit|)
|CTRL-W_r|	CTRL-W r	   rotate windows downwards N times
|CTRL-W_s|	CTRL-W s	   split current window in two parts, new window N lines high
|CTRL-W_t|	CTRL-W t	   go to top window
|CTRL-W_v|	CTRL-W v	   split current window vertically, new window N columns wide
|CTRL-W_w|	CTRL-W w	   go to N next window (wrap around)
|CTRL-W_x|	CTRL-W x	   exchange current window with window N (default: next window)
|CTRL-W_z|	CTRL-W z	   close preview window
|CTRL-W_bar|	CTRL-W |	   set window width to N columns
|CTRL-W_}|	CTRL-W }	   show tag under cursor in preview window
|CTRL-W_<Down>|	CTRL-W <Down>	   same as "CTRL-W j"
|CTRL-W_<Up>|	CTRL-W <Up>	   same as "CTRL-W k"
|CTRL-W_<Left>|	CTRL-W <Left>	   same as "CTRL-W h"
|CTRL-W_<Right>| CTRL-W <Right>	   same as "CTRL-W l"
|[_CTRL-D|	[ CTRL-D	   jump to first #define found in current and included files matching the word under the cursor, start searching at beginning of current file
|[_CTRL-I|	[ CTRL-I	   jump to first line in current and included files that contains the word under the cursor, start searching at beginning of current file
|[#|		[#		1  cursor to N previous unmatched #if, #else or #ifdef
|['|		['		1  cursor to previous lowercase mark, on first non-blank
|[(|		[(		1  cursor N times back to unmatched '('
|[star|		[*		1  same as "[/"
|[`|		[`		1  cursor to previous lowercase mark
|[/|		[/		1  cursor to N previous start of a C comment
|[D|		[D		   list all defines found in current and included files matching the word under the cursor, start searching at beginning of current file
|[I|		[I		   list all lines found in current and included files that contain the word under the cursor, start searching at beginning of current file
|[P|		[P		2  same as "[p"
|[[|		[[		1  cursor N sections backward
|[]|		[]		1  cursor N SECTIONS backward
|[c|		[c		1  cursor N times backwards to start of change
|[d|		[d		   show first #define found in current and included files matching the word under the cursor, start searching at beginning of current file
|[f|		[f		   same as "gf"
|[i|		[i		   show first line found in current and included files that contains the word under the cursor, start searching at beginning of current file
|[m|		[m		1  cursor N times back to start of member function
|[p|		[p		2  like "P", but adjust indent to current line
|[s|		[s		1  move to the previous misspelled word
|[z|		[z		1  move to start of open fold
|[{|		[{		1  cursor N times back to unmatched '{'
|]_CTRL-D|	] CTRL-D	   jump to first #define found in current and included files matching the word under the cursor, start searching at cursor position
|]_CTRL-I|	] CTRL-I	   jump to first line in current and included files that contains the word under the cursor, start searching at cursor position
|]#|		]#		1  cursor to N next unmatched #endif or #else
|]'|		]'		1  cursor to next lowercase mark, on first non-blank
|])|		])		1  cursor N times forward to unmatched ')'
|]star|		]*		1  same as "]/"
|]`|		]`		1  cursor to next lowercase mark
|]/|		]/		1  cursor to N next end of a C comment
|]D|		]D		   list all #defines found in current and included files matching the word under the cursor, start searching at cursor position
|]I|		]I		   list all lines found in current and included files that contain the word under the cursor, start searching at cursor position
|]P|		]P		2  same as "[p"
|][|		][		1  cursor N SECTIONS forward
|]]|		]]		1  cursor N sections forward
|]c|		]c		1  cursor N times forward to start of change
|]d|		]d		   show first #define found in current and included files matching the word under the cursor, start searching at cursor position
|]f|		]f		   same as "gf"
|]i|		]i		   show first line found in current and included files that contains the word under the cursor, start searching at cursor position
|]m|		]m		1  cursor N times forward to end of member function
|]p|		]p		2  like "p", but adjust indent to current line
|]s|		]s		1  move to next misspelled word
|]z|		]z		1  move to end of open fold
|]}|		]}		1  cursor N times forward to unmatched '}'
g_CTRL-A	g CTRL-A	   dump a memory profile
|g_CTRL-G|	g CTRL-G	   show information about current cursor position
|g_CTRL-H|	g CTRL-H	   start Select block mode
|g_CTRL-]|	g CTRL-]	   |:tjump| to the tag under the cursor
|g#|		g#		1  like "#", but without using "\<" and "\>"
|g$|		g$		1  when 'wrap' off go to rightmost character of the current line that is on the screen; when 'wrap' on go to the rightmost character of the current screen line
|g&|		g&		2  repeat last ":s" on all lines
|g'|		g'{mark}	1  like |'| but without changing the jumplist
|g`|		g`{mark}	1  like |`| but without changing the jumplist
|gstar|		g*		1  like "*", but without using "\<" and "\>"
|g+|		g+		   go to newer text state N times
|g,|		g,		1  go to N newer position in change list
|g-|		g-		   go to older text state N times
|g0|		g0		1  when 'wrap' off go to leftmost character of the current line that is on the screen; when 'wrap' on go to the leftmost character of the current screen line
|g8|		g8		   print hex value of bytes used in UTF-8 character under the cursor
|g;|		g;		1  go to N older position in change list
|g<|		g<		   display previous command output
|g?|		g?		2  Rot13 encoding operator
|g?g?|		g??		2  Rot13 encode current line
|g?g?|		g?g?		2  Rot13 encode current line
|gD|		gD		1  go to definition of word under the cursor in current file
|gE|		gE		1  go backwards to the end of the previous WORD
|gH|		gH		   start Select line mode
|gI|		gI		2  like "I", but always start in column 1
|gJ|		gJ		2  join lines without inserting space
|gN|		gN	      1,2  find the previous match with the last used search pattern and Visually select it
|gP|		["x]gP		2  put the text [from register x] before the cursor N times, leave the cursor after it
|gQ|		gQ		    switch to "Ex" mode with Vim editing
|gR|		gR		2  enter Virtual Replace mode
|gT|		gT		   go to the previous tab page
|gU|		gU{motion}	2  make Nmove text uppercase
|gV|		gV		   don't reselect the previous Visual area when executing a mapping or menu in Select mode
|g]|		g]		   :tselect on the tag under the cursor
|g^|		g^		1  when 'wrap' off go to leftmost non-white character of the current line that is on the screen; when 'wrap' on go to the leftmost non-white character of the current screen line
|g_|		g_		1  cursor to the last CHAR N - 1 lines lower
|ga|		ga		   print ascii value of character under the cursor
|gd|		gd		1  go to definition of word under the cursor in current function
|ge|		ge		1  go backwards to the end of the previous word
|gf|		gf		   start editing the file whose name is under the cursor
|gF|		gF		   start editing the file whose name is under the cursor and jump to the line number following the filename.
|gg|		gg		1  cursor to line N, default first line
|gh|		gh		   start Select mode
|gi|		gi		2  like "i", but first move to the |'^| mark
|gj|		gj		1  like "j", but when 'wrap' on go N screen lines down
|gk|		gk		1  like "k", but when 'wrap' on go N screen lines up
|gm|		gm		1  go to character at middle of the screenline
|gM|		gM		1  go to character at middle of the text line
|gn|		gn	      1,2  find the next match with the last used search pattern and Visually select it
|go|		go		1  cursor to byte N in the buffer
|gp|		["x]gp		2  put the text [from register x] after the cursor N times, leave the cursor after it
|gq|		gq{motion}	2  format Nmove text
|gr|		gr{char}	2  virtual replace N chars with {char}
|gs|		gs		   go to sleep for N seconds (default 1)
|gt|		gt		   go to the next tab page
|gu|		gu{motion}	2  make Nmove text lowercase
|gv|		gv		   reselect the previous Visual area
|gw|		gw{motion}	2  format Nmove text and keep cursor
|netrw-gx|	gx		   execute application for file name under the cursor (only with |netrw| plugin)
|g@|		g@{motion}	   call 'operatorfunc'
|g~|		g~{motion}	2  swap case for Nmove text
|g<Down>|	g<Down>		1  same as "gj"
|g<End>|	g<End>		1  same as "g$"
|g<Home>|	g<Home>		1  same as "g0"
|g<Tab>|	g<Tab>		   go to last accessed tab page
|g<Up>|		g<Up>		1  same as "gk"
|z<CR>|		z<CR>		   redraw, cursor line to top of window, cursor on first non-blank
|zN<CR>|	z{height}<CR>	   redraw, make window {height} lines high
|z+|		z+		   cursor on line N (default line below window), otherwise like "z<CR>"
|z-|		z-		   redraw, cursor line at bottom of window, cursor on first non-blank
|z.|		z.		   redraw, cursor line to center of window, cursor on first non-blank
|z=|		z=		   give spelling suggestions
|zA|		zA		   open a closed fold or close an open fold recursively
|zC|		zC		   close folds recursively
|zD|		zD		   delete folds recursively
|zE|		zE		   eliminate all folds
|zF|		zF		   create a fold for N lines
|zG|		zG		   temporarily mark word as correctly spelled
|zH|		zH		   when 'wrap' off scroll half a screenwidth to the right
|zL|		zL		   when 'wrap' off scroll half a screenwidth to the left
|zM|		zM		   set 'foldlevel' to zero
|zN|		zN		   set 'foldenable'
|zO|		zO		   open folds recursively
|zR|		zR		   set 'foldlevel' to the deepest fold
|zW|		zW		   temporarily mark word as incorrectly spelled
|zX|		zX		   re-apply 'foldlevel'
|z^|		z^		   cursor on line N (default line above window), otherwise like "z-"
|za|		za		   open a closed fold, close an open fold
|zb|		zb		   redraw, cursor line at bottom of window
|zc|		zc		   close a fold
|zd|		zd		   delete a fold
|ze|		ze		   when 'wrap' off scroll horizontally to position the cursor at the end (right side) of the screen
|zf|		zf{motion}	   create a fold for Nmove text
|zg|		zg		   permanently mark word as correctly spelled
|zh|		zh		   when 'wrap' off scroll screen N characters to the right
|zi|		zi		   toggle 'foldenable'
|zj|		zj		1  move to the start of the next fold
|zk|		zk		1  move to the end of the previous fold
|zl|		zl		   when 'wrap' off scroll screen N characters to the left
|zm|		zm		   subtract one from 'foldlevel'
|zn|		zn		   reset 'foldenable'
|zo|		zo		   open fold
|zp|		zp		   paste in block-mode without trailing spaces
|zP|		zP		   paste in block-mode without trailing spaces
|zr|		zr		   add one to 'foldlevel'
|zs|		zs		   when 'wrap' off scroll horizontally to position the cursor at the start (left side) of the screen
|zt|		zt		   redraw, cursor line at top of window
|zuw|		zuw		   undo |zw|
|zug|		zug		   undo |zg|
|zuW|		zuW		   undo |zW|
|zuG|		zuG		   undo |zG|
|zv|		zv		   open enough folds to view the cursor line
|zw|		zw		   permanently mark word as incorrectly spelled
|zx|		zx		   re-apply 'foldlevel' and do "zv"
|zy|		zy		   yank without trailing spaces
|zz|		zz		   redraw, cursor line at center of window
|z<Left>|	z<Left>		   same as "zh"
|z<Right>|	z<Right>	   same as "zl"
|o_v|		v		force operator to work charwise
|o_V|		V		force operator to work linewise
|o_CTRL-V|	CTRL-V		force operator to work blockwise
|v_CTRL-\_CTRL-N| CTRL-\ CTRL-N	   stop Visual mode
|v_CTRL-\_CTRL-G| CTRL-\ CTRL-G	   go to Normal mode
|v_CTRL-A|	CTRL-A		2  add N to number in highlighted text
|v_CTRL-C|	CTRL-C		   stop Visual mode
|v_CTRL-G|	CTRL-G		   toggle between Visual mode and Select mode
|v_<BS>|	<BS>		2  Select mode: delete highlighted area
|v_CTRL-H|	CTRL-H		2  same as <BS>
|v_CTRL-O|	CTRL-O		   switch from Select to Visual mode for one command
|v_CTRL-V|	CTRL-V		   make Visual mode blockwise or stop Visual mode
|v_CTRL-X|	CTRL-X		2  subtract N from number in highlighted text
|v_<Esc>|	<Esc>		   stop Visual mode
|v_CTRL-]|	CTRL-]		   jump to highlighted tag
|v_!|		!{filter}	2  filter the highlighted lines through the external command {filter}
|v_:|		:		   start a command-line with the highlighted lines as a range
|v_<|		<		2  shift the highlighted lines one 'shiftwidth' left
|v_=|		=		2  filter the highlighted lines through the external program given with the 'equalprg' option
|v_>|		>		2  shift the highlighted lines one 'shiftwidth' right
|v_b_A|		A		2  block mode: append same text in all lines, after the highlighted area
|v_C|		C		2  delete the highlighted lines and start insert
|v_D|		D		2  delete the highlighted lines
|v_b_I|		I		2  block mode: insert same text in all lines, before the highlighted area
|v_J|		J		2  join the highlighted lines
|v_K|		K		   run 'keywordprg' on the highlighted area
|v_O|		O		   move horizontally to other corner of area
|v_P|		P		   replace highlighted area with register contents; registers are unchanged
|v_R|		R		2  delete the highlighted lines and start insert
|v_S|		S		2  delete the highlighted lines and start insert
|v_U|		U		2  make highlighted area uppercase
|v_V|		V		   make Visual mode linewise or stop Visual mode
|v_X|		X		2  delete the highlighted lines
|v_Y|		Y		   yank the highlighted lines
|v_aquote|	a"		   extend highlighted area with a double quoted string
|v_a'|		a'		   extend highlighted area with a single quoted string
|v_a(|		a(		   same as ab
|v_a)|		a)		   same as ab
|v_a<|		a<		   extend highlighted area with a <> block
|v_a>|		a>		   same as a<
|v_aB|		aB		   extend highlighted area with a {} block
|v_aW|		aW		   extend highlighted area with "a WORD"
|v_a[|		a[		   extend highlighted area with a [] block
|v_a]|		a]		   same as a[
|v_a`|		a`		   extend highlighted area with a backtick quoted string
|v_ab|		ab		   extend highlighted area with a () block
|v_ap|		ap		   extend highlighted area with a paragraph
|v_as|		as		   extend highlighted area with a sentence
|v_at|		at		   extend highlighted area with a tag block
|v_aw|		aw		   extend highlighted area with "a word"
|v_a{|		a{		   same as aB
|v_a}|		a}		   same as aB
|v_c|		c		2  delete highlighted area and start insert
|v_d|		d		2  delete highlighted area
|v_g_CTRL-A|	g CTRL-A	2  add N to number in highlighted text
|v_g_CTRL-X|	g CTRL-X	2  subtract N from number in highlighted text
|v_gJ|		gJ		2  join the highlighted lines without inserting spaces
|v_gq|		gq		2  format the highlighted lines
|v_gv|		gv		   exchange current and previous highlighted area
|v_iquote|	i"		   extend highlighted area with a double quoted string (without quotes)
|v_i'|		i'		   extend highlighted area with a single quoted string (without quotes)
|v_i(|		i(		   same as ib
|v_i)|		i)		   same as ib
|v_i<|		i<		   extend highlighted area with inner <> block
|v_i>|		i>		   same as i<
|v_iB|		iB		   extend highlighted area with inner {} block
|v_iW|		iW		   extend highlighted area with "inner WORD"
|v_i[|		i[		   extend highlighted area with inner [] block
|v_i]|		i]		   same as i[
|v_i`|		i`		   extend highlighted area with a backtick quoted string (without the backticks)
|v_ib|		ib		   extend highlighted area with inner () block
|v_ip|		ip		   extend highlighted area with inner paragraph
|v_is|		is		   extend highlighted area with inner sentence
|v_it|		it		   extend highlighted area with inner tag block
|v_iw|		iw		   extend highlighted area with "inner word"
|v_i{|		i{		   same as iB
|v_i}|		i}		   same as iB
|v_o|		o		   move cursor to other corner of area
|v_p|		p		   replace highlighted area with register contents; deleted text in unnamed register
|v_r|		r		2  replace highlighted area with a character
|v_s|		s		2  delete highlighted area and start insert
|v_u|		u		2  make highlighted area lowercase
|v_v|		v		   make Visual mode charwise or stop Visual mode
|v_x|		x		2  delete the highlighted area
|v_y|		y		   yank the highlighted area
|v_~|		~		2  swap case for the highlighted area
|c_CTRL-A|	CTRL-A		do completion on the pattern in front of the cursor and insert all matches
|c_CTRL-B|	CTRL-B		cursor to begin of command-line
|c_CTRL-C|	CTRL-C		same as <Esc>
|c_CTRL-D|	CTRL-D		list completions that match the pattern in front of the cursor
|c_CTRL-E|	CTRL-E		cursor to end of command-line
|'cedit'|	CTRL-F		default value for 'cedit': opens the command-line window; otherwise not used
|c_CTRL-G|	CTRL-G		next match when 'incsearch' is active
|c_<BS>|	<BS>		delete the character in front of the cursor
|c_digraph|	{char1} <BS> {char2} enter digraph when 'digraph' is on
|c_CTRL-H|	CTRL-H		same as <BS>
|c_<Tab>|	<Tab>		if 'wildchar' is <Tab>: Do completion on the pattern in front of the cursor
|c_<S-Tab>|	<S-Tab>		same as CTRL-P
|c_wildchar|	'wildchar'	Do completion on the pattern in front of the cursor (default: <Tab>)
|c_CTRL-I|	CTRL-I		same as <Tab>
|c_<NL>|	<NL>		same as <CR>
|c_CTRL-J|	CTRL-J		same as <CR>
|c_CTRL-K|	CTRL-K {char1} {char2} enter digraph
|c_CTRL-L|	CTRL-L		do completion on the pattern in front of the cursor and insert the longest common part
|c_<CR>|	<CR>		execute entered command
|c_CTRL-M|	CTRL-M		same as <CR>
|c_CTRL-N|	CTRL-N		after using 'wildchar' with multiple matches: go to next match, otherwise: recall older command-line from history.
|c_CTRL-P|	CTRL-P		after using 'wildchar' with multiple matches: go to previous match, otherwise: recall older command-line from history.
|c_CTRL-Q|	CTRL-Q		same as CTRL-V, unless it's used for terminal control flow
|c_CTRL-R|	CTRL-R {regname} insert the contents of a register or object under the cursor as if typed
|c_CTRL-R_CTRL-R| CTRL-R CTRL-R {regname}
|c_CTRL-R_CTRL-O| CTRL-R CTRL-O {regname} insert the contents of a register or object under the cursor literally
|c_CTRL-T|	CTRL-T		previous match when 'incsearch' is active
|c_CTRL-U|	CTRL-U		remove all characters
|c_CTRL-V|	CTRL-V		insert next non-digit literally, insert three digit decimal number as a single byte.
|c_CTRL-W|	CTRL-W		delete the word in front of the cursor
CTRL-Y		copy (yank) modeless selection
|c_<Esc>|	<Esc>		abandon command-line without executing it
|c_CTRL-[|	CTRL-[		same as <Esc>
|c_CTRL-\_CTRL-N| CTRL-\ CTRL-N	go to Normal mode, abandon command-line
|c_CTRL-\_CTRL-G| CTRL-\ CTRL-G	go to Normal mode, abandon command-line
|c_CTRL-\_e|	CTRL-\ e {expr} replace the command line with the result of {expr}
|c_CTRL-]|	CTRL-]		trigger abbreviation
|c_CTRL-^|	CTRL-^		toggle use of |:lmap| mappings
|c_CTRL-_|	CTRL-_		when 'allowrevins' set: change language (Hebrew)
|c_<Del>|	<Del>		delete the character under the cursor
|c_<Left>|	<Left>		cursor left
|c_<S-Left>|	<S-Left>	cursor one word left
|c_<C-Left>|	<C-Left>	cursor one word left
|c_<Right>|	<Right>		cursor right
|c_<S-Right>|	<S-Right>	cursor one word right
|c_<C-Right>|	<C-Right>	cursor one word right
|c_<Up>|	<Up>		recall previous command-line from history that matches pattern in front of the cursor
|c_<S-Up>|	<S-Up>		recall previous command-line from history
|c_<Down>|	<Down>		recall next command-line from history that matches pattern in front of the cursor
|c_<S-Down>|	<S-Down>	recall next command-line from history
|c_<Home>|	<Home>		cursor to start of command-line
|c_<End>|	<End>		cursor to end of command-line
|c_<PageDown>|	<PageDown>	same as <S-Down>
|c_<PageUp>|	<PageUp>	same as <S-Up>
|c_<Insert>|	<Insert>	toggle insert/overstrike mode
In a |terminal| buffer all keys except CTRL-\ are forwarded to the terminal job.  If CTRL-\ is pressed, the next key is forwarded unless it is CTRL-N or CTRL-O.
In terminal buffer use |CTRL-\_CTRL-N| to go to Normal mode.
In terminal buffer use |t_CTRL-\_CTRL-O| to execute one normal mode command and then return to terminal mode.
|:range|	:{range}	go to last line in {range}
|:!|		:!		filter lines or execute an external command
|:!!|		:!!		repeat last ":!" command
|:#|		:#		same as ":number"
|:&|		:&		repeat last ":substitute"
|:star|		:*		use the last Visual area, like :'<,'>
|:<|		:<		shift lines one 'shiftwidth' left
|:=|		:=		print the last line number
|:>|		:>		shift lines one 'shiftwidth' right
|:@|		:@		execute contents of a register
|:@@|		:@@		repeat the previous ":@"
|:Next|		:N[ext]		go to previous file in the argument list
|:append|	:a[ppend]	append text
|:abbreviate|	:ab[breviate]	enter abbreviation
|:abclear|	:abc[lear]	remove all abbreviations
|:aboveleft|	:abo[veleft]	make split window appear left or above
|:all|		:al[l]		open a window for each file in the argument list
|:amenu|	:am[enu]	enter new menu item for all modes
|:anoremenu|	:an[oremenu]	enter a new menu for all modes that will not be remapped
|:args|		:ar[gs]		print the argument list
|:argadd|	:arga[dd]	add items to the argument list
|:argdedupe|	:argded[upe]	remove duplicates from the argument list
|:argdelete|	:argd[elete]	delete items from the argument list
|:argedit|	:arge[dit]	add item to the argument list and edit it
|:argdo|	:argdo		do a command on all items in the argument list
|:argglobal|	:argg[lobal]	define the global argument list
|:arglocal|	:argl[ocal]	define a local argument list
|:argument|	:argu[ment]	go to specific file in the argument list
|:ascii|	:as[cii]	print ascii value of character under the cursor
|:autocmd|	:au[tocmd]	enter or show autocommands
|:augroup|	:aug[roup]	select the autocommand group to use
|:aunmenu|	:aun[menu]	remove menu for all modes
|:buffer|	:b[uffer]	go to specific buffer in the buffer list
|:bNext|	:bN[ext]	go to previous buffer in the buffer list
|:ball|		:ba[ll]		open a window for each buffer in the buffer list
|:badd|		:bad[d]		add buffer to the buffer list
|:balt|		:balt		like ":badd" but also set the alternate file
|:bdelete|	:bd[elete]	remove a buffer from the buffer list
|:behave|	:be[have]	set mouse and selection behavior
|:belowright|	:bel[owright]	make split window appear right or below
|:bfirst|	:bf[irst]	go to first buffer in the buffer list
|:blast|	:bl[ast]	go to last buffer in the buffer list
|:bmodified|	:bm[odified]	go to next buffer in the buffer list that has been modified
|:bnext|	:bn[ext]	go to next buffer in the buffer list
|:botright|	:bo[tright]	make split window appear at bottom or far right
|:bprevious|	:bp[revious]	go to previous buffer in the buffer list
|:brewind|	:br[ewind]	go to first buffer in the buffer list
|:break|	:brea[k]	break out of while loop
|:breakadd|	:breaka[dd]	add a debugger breakpoint
|:breakdel|	:breakd[el]	delete a debugger breakpoint
|:breaklist|	:breakl[ist]	list debugger breakpoints
|:browse|	:bro[wse]	use file selection dialog
|:bufdo|	:bufdo		execute command in each listed buffer
|:buffers|	:buffers	list all files in the buffer list
|:bunload|	:bun[load]	unload a specific buffer
|:bwipeout|	:bw[ipeout]	really delete a buffer
|:change|	:c[hange]	replace a line or series of lines
|:cNext|	:cN[ext]	go to previous error
|:cNfile|	:cNf[ile]	go to last error in previous file
|:cabbrev|	:ca[bbrev]	like ":abbreviate" but for Command-line mode
|:cabclear|	:cabc[lear]	clear all abbreviations for Command-line mode
|:cabove|	:cabo[ve]	go to error above current line
|:caddbuffer|	:cad[dbuffer]	add errors from buffer
|:caddexpr|	:cadde[xpr]	add errors from expr
|:caddfile|	:caddf[ile]	add error message to current quickfix list
|:cafter|	:caf[ter]	go to error after current cursor
|:call|		:cal[l]		call a function
|:catch|	:cat[ch]	part of a :try command
|:cbefore|	:cbef[ore]	go to error before current cursor
|:cbelow|	:cbel[ow]	go to error below current line
|:cbottom|	:cbo[ttom]	scroll to the bottom of the quickfix window
|:cbuffer|	:cb[uffer]	parse error messages and jump to first error
|:cc|		:cc		go to specific error
|:cclose|	:ccl[ose]	close quickfix window
|:cd|		:cd		change directory
|:cdo|		:cdo		execute command in each valid error list entry
|:cfdo|		:cfd[o]		execute command in each file in error list
|:center|	:ce[nter]	format lines at the center
|:cexpr|	:cex[pr]	read errors from expr and jump to first
|:cfile|	:cf[ile]	read file with error messages and jump to first
|:cfirst|	:cfir[st]	go to the specified error, default first one
|:cgetbuffer|	:cgetb[uffer]	get errors from buffer
|:cgetexpr|	:cgete[xpr]	get errors from expr
|:cgetfile|	:cg[etfile]	read file with error messages
|:changes|	:changes	print the change list
|:chdir|	:chd[ir]	change directory
|:checkhealth|	:che[ckhealth]	run healthchecks
|:checkpath|	:checkp[ath]	list included files
|:checktime|	:checkt[ime]	check timestamp of loaded buffers
|:chistory|	:chi[story]	list the error lists
|:clast|	:cla[st]	go to the specified error, default last one
|:clearjumps|	:cle[arjumps]	clear the jump list
|:clist|	:cl[ist]	list all errors
|:close|	:clo[se]	close current window
|:cmap|		:cm[ap]		like ":map" but for Command-line mode
|:cmapclear|	:cmapc[lear]	clear all mappings for Command-line mode
|:cmenu|	:cme[nu]	add menu for Command-line mode
|:cnext|	:cn[ext]	go to next error
|:cnewer|	:cnew[er]	go to newer error list
|:cnfile|	:cnf[ile]	go to first error in next file
|:cnoremap|	:cno[remap]	like ":noremap" but for Command-line mode
|:cnoreabbrev|	:cnorea[bbrev]	like ":noreabbrev" but for Command-line mode
|:cnoremenu|	:cnoreme[nu]	like ":noremenu" but for Command-line mode
|:copy|		:co[py]		copy lines
|:colder|	:col[der]	go to older error list
|:colorscheme|	:colo[rscheme]	load a specific color scheme
|:command|	:com[mand]	create user-defined command
|:comclear|	:comc[lear]	clear all user-defined commands
|:compiler|	:comp[iler]	do settings for a specific compiler
|:continue|	:con[tinue]	go back to :while
|:confirm|	:conf[irm]	prompt user when confirmation required
|:const|	:cons[t]	create a variable as a constant
|:copen|	:cope[n]	open quickfix window
|:cprevious|	:cp[revious]	go to previous error
|:cpfile|	:cpf[ile]	go to last error in previous file
|:cquit|	:cq[uit]	quit Vim with an error code
|:crewind|	:cr[ewind]	go to the specified error, default first one
|:cunmap|	:cu[nmap]	like ":unmap" but for Command-line mode
|:cunabbrev|	:cuna[bbrev]	like ":unabbrev" but for Command-line mode
|:cunmenu|	:cunme[nu]	remove menu for Command-line mode
|:cwindow|	:cw[indow]	open or close quickfix window
|:delete|	:d[elete]	delete lines
|:debug|	:deb[ug]	run a command in debugging mode
|:debuggreedy|	:debugg[reedy]	read debug mode commands from normal input
|:delcommand|	:delc[ommand]	delete user-defined command
|:delfunction|	:delf[unction]	delete a user function
|:delmarks|	:delm[arks]	delete marks
|:diffupdate|	:dif[fupdate]	update 'diff' buffers
|:diffget|	:diffg[et]	remove differences in current buffer
|:diffoff|	:diffo[ff]	switch off diff mode
|:diffpatch|	:diffp[atch]	apply a patch and show differences
|:diffput|	:diffpu[t]	remove differences in other buffer
|:diffsplit|	:diffs[plit]	show differences with another file
|:diffthis|	:diffthis	make current window a diff window
|:digraphs|	:dig[raphs]	show or enter digraphs
|:display|	:di[splay]	display registers
|:djump|	:dj[ump]	jump to #define
|:dl|		:dl		short for |:delete| with the 'l' flag
|:dlist|	:dli[st]	list #defines
|:doautocmd|	:do[autocmd]	apply autocommands to current buffer
|:doautoall|	:doautoa[ll]	apply autocommands for all loaded buffers
|:dp|		:d[elete]p	short for |:delete| with the 'p' flag
|:drop|		:dr[op]		jump to window editing file or edit file in current window
|:dsearch|	:ds[earch]	list one #define
|:dsplit|	:dsp[lit]	split window and jump to #define
|:edit|		:e[dit]		edit a file
|:earlier|	:ea[rlier]	go to older change, undo
|:echo|		:ec[ho]		echoes the result of expressions
|:echoerr|	:echoe[rr]	like :echo, show like an error and use history
|:echohl|	:echoh[l]	set highlighting for echo commands
|:echomsg|	:echom[sg]	same as :echo, put message in history
|:echon|	:echon		same as :echo, but without <EOL>
|:else|		:el[se]		part of an :if command
|:elseif|	:elsei[f]	part of an :if command
|:emenu|	:em[enu]	execute a menu by name
|:endif|	:en[dif]	end previous :if
|:endfor|	:endfo[r]	end previous :for
|:endfunction|	:endf[unction]	end of a user function started with :function
|:endtry|	:endt[ry]	end previous :try
|:endwhile|	:endw[hile]	end previous :while
|:enew|		:ene[w]		edit a new, unnamed buffer
|:eval|		:ev[al]		evaluate an expression and discard the result
|:ex|		:ex		same as ":edit"
|:execute|	:exe[cute]	execute result of expressions
|:exit|		:exi[t]		same as ":xit"
|:exusage|	:exu[sage]	overview of Ex commands
|:file|		:f[ile]		show or set the current file name
|:files|	:files		list all files in the buffer list
|:filetype|	:filet[ype]	switch file type detection on/off
|:filter|	:filt[er]	filter output of following command
|:find|		:fin[d]		find file in 'path' and edit it
|:finally|	:fina[lly]	part of a :try command
|:finish|	:fini[sh]	quit sourcing a Vim script
|:first|	:fir[st]	go to the first file in the argument list
|:fold|		:fo[ld]		create a fold
|:foldclose|	:foldc[lose]	close folds
|:folddoopen|	:foldd[oopen]	execute command on lines not in a closed fold
|:folddoclosed|	:folddoc[losed]	execute command on lines in a closed fold
|:foldopen|	:foldo[pen]	open folds
|:for|		:for		for loop
|:function|	:fu[nction]	define a user function
|:global|	:g[lobal]	execute commands for matching lines
|:goto|		:go[to]		go to byte in the buffer
|:grep|		:gr[ep]		run 'grepprg' and jump to first match
|:grepadd|	:grepa[dd]	like :grep, but append to current list
|:gui|		:gu[i]		start the GUI
|:gvim|		:gv[im]		start the GUI
|:help|		:h[elp]		open a help window
|:helpclose|	:helpc[lose]	close one help window
|:helpgrep|	:helpg[rep]	like ":grep" but searches help files
|:helptags|	:helpt[ags]	generate help tags for a directory
|:highlight|	:hi[ghlight]	specify highlighting methods
|:hide|		:hid[e]		hide current buffer for a command
|:history|	:his[tory]	print a history list
|:horizontal|	:hor[izontal]	following window command work horizontally
|:insert|	:i[nsert]	insert text
|:iabbrev|	:ia[bbrev]	like ":abbrev" but for Insert mode
|:iabclear|	:iabc[lear]	like ":abclear" but for Insert mode
|:if|		:if		execute commands when condition met
|:ijump|	:ij[ump]	jump to definition of identifier
|:ilist|	:il[ist]	list lines where identifier matches
|:imap|		:im[ap]		like ":map" but for Insert mode
|:imapclear|	:imapc[lear]	like ":mapclear" but for Insert mode
|:imenu|	:ime[nu]	add menu for Insert mode
|:inoremap|	:ino[remap]	like ":noremap" but for Insert mode
|:inoreabbrev|	:inorea[bbrev]	like ":noreabbrev" but for Insert mode
|:inoremenu|	:inoreme[nu]	like ":noremenu" but for Insert mode
|:intro|	:int[ro]	print the introductory message
|:isearch|	:is[earch]	list one line where identifier matches
|:isplit|	:isp[lit]	split window and jump to definition of identifier
|:iunmap|	:iu[nmap]	like ":unmap" but for Insert mode
|:iunabbrev|	:iuna[bbrev]	like ":unabbrev" but for Insert mode
|:iunmenu|	:iunme[nu]	remove menu for Insert mode
|:join|		:j[oin]		join lines
|:jumps|	:ju[mps]	print the jump list
|:k|		:k		set a mark
|:keepalt|	:keepa[lt]	following command keeps the alternate file
|:keepmarks|	:kee[pmarks]	following command keeps marks where they are
|:keepjumps|	:keepj[umps]	following command keeps jumplist and marks
|:keeppatterns|	:keepp[atterns]	following command keeps search pattern history
|:lNext|	:lN[ext]	go to previous entry in location list
|:lNfile|	:lNf[ile]	go to last entry in previous file
|:list|		:l[ist]		print lines
|:labove|	:lab[ove]	go to location above current line
|:laddexpr|	:lad[dexpr]	add locations from expr
|:laddbuffer|	:laddb[uffer]	add locations from buffer
|:laddfile|	:laddf[ile]	add locations to current location list
|:lafter|	:laf[ter]	go to location after current cursor
|:last|		:la[st]		go to the last file in the argument list
|:language|	:lan[guage]	set the language (locale)
|:later|	:lat[er]	go to newer change, redo
|:lbefore|	:lbef[ore]	go to location before current cursor
|:lbelow|	:lbel[ow]	go to location below current line
|:lbottom|	:lbo[ttom]	scroll to the bottom of the location window
|:lbuffer|	:lb[uffer]	parse locations and jump to first location
|:lcd|		:lc[d]		change directory locally
|:lchdir|	:lch[dir]	change directory locally
|:lclose|	:lcl[ose]	close location window
|:ldo|		:ld[o]		execute command in valid location list entries
|:lfdo|		:lfd[o]		execute command in each file in location list
|:left|		:le[ft]		left align lines
|:leftabove|	:lefta[bove]	make split window appear left or above
|:let|		:let		assign a value to a variable or option
|:lexpr|	:lex[pr]	read locations from expr and jump to first
|:lfile|	:lf[ile]	read file with locations and jump to first
|:lfirst|	:lfir[st]	go to the specified location, default first one
|:lgetbuffer|	:lgetb[uffer]	get locations from buffer
|:lgetexpr|	:lgete[xpr]	get locations from expr
|:lgetfile|	:lg[etfile]	read file with locations
|:lgrep|	:lgr[ep]	run 'grepprg' and jump to first match
|:lgrepadd|	:lgrepa[dd]	like :grep, but append to current list
|:lhelpgrep|	:lh[elpgrep]	like ":helpgrep" but uses location list
|:lhistory|	:lhi[story]	list the location lists
|:ll|		:ll		go to specific location
|:llast|	:lla[st]	go to the specified location, default last one
|:llist|	:lli[st]	list all locations
|:lmake|	:lmak[e]	execute external command 'makeprg' and parse error messages
|:lmap|		:lm[ap]		like ":map!" but includes Lang-Arg mode
|:lmapclear|	:lmapc[lear]	like ":mapclear!" but includes Lang-Arg mode
|:lnext|	:lne[xt]	go to next location
|:lnewer|	:lnew[er]	go to newer location list
|:lnfile|	:lnf[ile]	go to first location in next file
|:lnoremap|	:ln[oremap]	like ":noremap!" but includes Lang-Arg mode
|:loadkeymap|	:loadk[eymap]	load the following keymaps until EOF
|:loadview|	:lo[adview]	load view for current window from a file
|:lockmarks|	:loc[kmarks]	following command keeps marks where they are
|:lockvar|	:lockv[ar]	lock variables
|:lolder|	:lol[der]	go to older location list
|:lopen|	:lope[n]	open location window
|:lprevious|	:lp[revious]	go to previous location
|:lpfile|	:lpf[ile]	go to last location in previous file
|:lrewind|	:lr[ewind]	go to the specified location, default first one
|:ls|		:ls		list all buffers
|:ltag|		:lt[ag]		jump to tag and add matching tags to the location list
|:lunmap|	:lu[nmap]	like ":unmap!" but includes Lang-Arg mode
|:lua|		:lua		execute |Lua| command
|:luado|	:luad[o]	execute Lua command for each line
|:luafile|	:luaf[ile]	execute |Lua| script file
|:lvimgrep|	:lv[imgrep]	search for pattern in files
|:lvimgrepadd|	:lvimgrepa[dd]	like :vimgrep, but append to current list
|:lwindow|	:lw[indow]	open or close location window
|:move|		:m[ove]		move lines
|:mark|		:ma[rk]		set a mark
|:make|		:mak[e]		execute external command 'makeprg' and parse error messages
|:map|		:map		show or enter a mapping
|:mapclear|	:mapc[lear]	clear all mappings for Normal and Visual mode
|:marks|	:marks		list all marks
|:match|	:mat[ch]	define a match to highlight
|:menu|		:me[nu]		enter a new menu item
|:menutranslate|  :menut[ranslate] add a menu translation item
|:messages|	:mes[sages]	view previously displayed messages
|:mkexrc|	:mk[exrc]	write current mappings and settings to a file
|:mksession|	:mks[ession]	write session info to a file
|:mkspell|	:mksp[ell]	produce .spl spell file
|:mkvimrc|	:mkv[imrc]	write current mappings and settings to a file
|:mkview|	:mkvie[w]	write view of current window to a file
|:mode|		:mod[e]		show or change the screen mode
|:next|		:n[ext]		go to next file in the argument list
|:new|		:new		create a new empty window
|:nmap|		:nm[ap]		like ":map" but for Normal mode
|:nmapclear|	:nmapc[lear]	clear all mappings for Normal mode
|:nmenu|	:nme[nu]	add menu for Normal mode
|:nnoremap|	:nn[oremap]	like ":noremap" but for Normal mode
|:nnoremenu|	:nnoreme[nu]	like ":noremenu" but for Normal mode
|:noautocmd|	:noa[utocmd]	following commands don't trigger autocommands
|:noremap|	:no[remap]	enter a mapping that will not be remapped
|:nohlsearch|	:noh[lsearch]	suspend 'hlsearch' highlighting
|:noreabbrev|	:norea[bbrev]	enter an abbreviation that will not be remapped
|:noremenu|	:noreme[nu]	enter a menu that will not be remapped
|:normal|	:norm[al]	execute Normal mode commands
|:noswapfile|	:nos[wapfile]	following commands don't create a swap file
|:number|	:nu[mber]	print lines with line number
|:nunmap|	:nun[map]	like ":unmap" but for Normal mode
|:nunmenu|	:nunme[nu]	remove menu for Normal mode
|:oldfiles|	:ol[dfiles]	list files that have marks in the |shada| file
|:omap|		:om[ap]		like ":map" but for Operator-pending mode
|:omapclear|	:omapc[lear]	remove all mappings for Operator-pending mode
|:omenu|	:ome[nu]	add menu for Operator-pending mode
|:only|		:on[ly]		close all windows except the current one
|:onoremap|	:ono[remap]	like ":noremap" but for Operator-pending mode
|:onoremenu|	:onoreme[nu]	like ":noremenu" but for Operator-pending mode
|:options|	:opt[ions]	open the options-window
|:ounmap|	:ou[nmap]	like ":unmap" but for Operator-pending mode
|:ounmenu|	:ounme[nu]	remove menu for Operator-pending mode
|:ownsyntax|	:ow[nsyntax]	set new local syntax highlight for this window
|:packadd|	:pa[ckadd]	add a plugin from 'packpath'
|:packloadall|	:packl[oadall]	load all packages under 'packpath'
|:pclose|	:pc[lose]	close preview window
|:pedit|	:ped[it]	edit file in the preview window
|:perl|		:pe[rl]		execute perl command
|:perldo|	:perld[o]	execute perl command for each line
|:perlfile|	:perlf[ile]	execute perl script file
|:print|	:p[rint]	print lines
|:profdel|	:profd[el]	stop profiling a function or script
|:profile|	:prof[ile]	profiling functions and scripts
|:pop|		:po[p]		jump to older entry in tag stack
|:popup|	:popu[p]	popup a menu by name
|:ppop|		:pp[op]		":pop" in preview window
|:preserve|	:pre[serve]	write all text to swap file
|:previous|	:prev[ious]	go to previous file in argument list
|:psearch|	:ps[earch]	like ":ijump" but shows match in preview window
|:ptag|		:pt[ag]		show tag in preview window
|:ptNext|	:ptN[ext]	|:tNext| in preview window
|:ptfirst|	:ptf[irst]	|:trewind| in preview window
|:ptjump|	:ptj[ump]	|:tjump| and show tag in preview window
|:ptlast|	:ptl[ast]	|:tlast| in preview window
|:ptnext|	:ptn[ext]	|:tnext| in preview window
|:ptprevious|	:ptp[revious]	|:tprevious| in preview window
|:ptrewind|	:ptr[ewind]	|:trewind| in preview window
|:ptselect|	:pts[elect]	|:tselect| and show tag in preview window
|:put|		:pu[t]		insert contents of register in the text
|:pwd|		:pw[d]		print current directory
|:py3|		:py3		execute Python 3 command
|:python3|	:python3	same as :py3
|:py3do|	:py3d[o]	execute Python 3 command for each line
|:py3file|	:py3f[ile]	execute Python 3 script file
|:python|	:py[thon]	execute Python command
|:pydo|		:pyd[o]		execute Python command for each line
|:pyfile|	:pyf[ile]	execute Python script file
|:pyx|		:pyx		execute |python_x| command
|:pythonx|	:pythonx	same as :pyx
|:pyxdo|	:pyxd[o]	execute |python_x| command for each line
|:pyxfile|	:pyxf[ile]	execute |python_x| script file
|:quit|		:q[uit]		quit current window (when one window quit Vim)
|:quitall|	:quita[ll]	quit Vim
|:qall|		:qa[ll]		quit Vim
|:read|		:r[ead]		read file into the text
|:recover|	:rec[over]	recover a file from a swap file
|:redo|		:red[o]		redo one undone change
|:redir|	:redi[r]	redirect messages to a file or register
|:redraw|	:redr[aw]	force a redraw of the display
|:redrawstatus|	:redraws[tatus]	force a redraw of the status line(s) and window bar(s)
|:redrawtabline|  :redrawt[abline]  force a redraw of the tabline
|:registers|	:reg[isters]	display the contents of registers
|:resize|	:res[ize]	change current window height
|:retab|	:ret[ab]	change tab size
|:return|	:retu[rn]	return from a user function
|:rewind|	:rew[ind]	go to the first file in the argument list
|:right|	:ri[ght]	right align text
|:rightbelow|	:rightb[elow]	make split window appear right or below
|:rshada|	:rsh[ada]	read from |shada| file
|:ruby|		:rub[y]		execute Ruby command
|:rubydo|	:rubyd[o]	execute Ruby command for each line
|:rubyfile|	:rubyf[ile]	execute Ruby script file
|:rundo|	:rund[o]	read undo information from a file
|:runtime|	:ru[ntime]	source vim scripts in 'runtimepath'
|:substitute|	:s[ubstitute]	find and replace text
|:sNext|	:sN[ext]	split window and go to previous file in argument list
|:sandbox|	:san[dbox]	execute a command in the sandbox
|:sargument|	:sa[rgument]	split window and go to specific file in argument list
|:sall|		:sal[l]		open a window for each file in argument list
|:saveas|	:sav[eas]	save file under another name.
|:sbuffer|	:sb[uffer]	split window and go to specific file in the buffer list
|:sbNext|	:sbN[ext]	split window and go to previous file in the buffer list
|:sball|	:sba[ll]	open a window for each file in the buffer list
|:sbfirst|	:sbf[irst]	split window and go to first file in the buffer list
|:sblast|	:sbl[ast]	split window and go to last file in buffer list
|:sbmodified|	:sbm[odified]	split window and go to modified file in the buffer list
|:sbnext|	:sbn[ext]	split window and go to next file in the buffer list
|:sbprevious|	:sbp[revious]	split window and go to previous file in the buffer list
|:sbrewind|	:sbr[ewind]	split window and go to first file in the buffer list
|:scriptnames|	:scr[iptnames]	list names of all sourced Vim scripts
|:scriptencoding| :scripte[ncoding]  encoding used in sourced Vim script
|:set|		:se[t]		show or set options
|:setfiletype|	:setf[iletype]	set 'filetype', unless it was set already
|:setglobal|	:setg[lobal]	show global values of options
|:setlocal|	:setl[ocal]	show or set options locally
|:sfind|	:sf[ind]	split current window and edit file in 'path'
|:sfirst|	:sfir[st]	split window and go to first file in the argument list
|:sign|		:sig[n]		manipulate signs
|:silent|	:sil[ent]	run a command silently
|:sleep|	:sl[eep]	do nothing for a few seconds
|:slast|	:sla[st]	split window and go to last file in the argument list
|:smagic|	:sm[agic]	:substitute with 'magic'
|:smap|		:smap		like ":map" but for Select mode
|:smapclear|	:smapc[lear]	remove all mappings for Select mode
|:smenu|	:sme[nu]	add menu for Select mode
|:snext|	:sn[ext]	split window and go to next file in the argument list
|:snomagic|	:sno[magic]	:substitute with 'nomagic'
|:snoremap|	:snor[emap]	like ":noremap" but for Select mode
|:snoremenu|	:snoreme[nu]	like ":noremenu" but for Select mode
|:sort|		:sor[t]		sort lines
|:source|	:so[urce]	read Vim or Ex commands from a file
|:spelldump|	:spelld[ump]	split window and fill with all correct words
|:spellgood|	:spe[llgood]	add good word for spelling
|:spellinfo|	:spelli[nfo]	show info about loaded spell files
|:spellrare|	:spellra[re]	add rare word for spelling
|:spellrepall|	:spellr[epall]	replace all bad words like last |z=|
|:spellundo|	:spellu[ndo]	remove good or bad word
|:spellwrong|	:spellw[rong]	add spelling mistake
|:split|	:sp[lit]	split current window
|:sprevious|	:spr[evious]	split window and go to previous file in the argument list
|:srewind|	:sre[wind]	split window and go to first file in the argument list
|:stop|		:st[op]		suspend the editor or escape to a shell
|:stag|		:sta[g]		split window and jump to a tag
|:startinsert|	:star[tinsert]	start Insert mode
|:startgreplace|  :startg[replace] start Virtual Replace mode
|:startreplace|	:startr[eplace]	start Replace mode
|:stopinsert|	:stopi[nsert]	stop Insert mode
|:stjump|	:stj[ump]	do ":tjump" and split window
|:stselect|	:sts[elect]	do ":tselect" and split window
|:sunhide|	:sun[hide]	same as ":unhide"
|:sunmap|	:sunm[ap]	like ":unmap" but for Select mode
|:sunmenu|	:sunme[nu]	remove menu for Select mode
|:suspend|	:sus[pend]	same as ":stop"
|:sview|	:sv[iew]	split window and edit file read-only
|:swapname|	:sw[apname]	show the name of the current swap file
|:syntax|	:sy[ntax]	syntax highlighting
|:syntime|	:synti[me]	measure syntax highlighting speed
|:syncbind|	:sync[bind]	sync scroll binding
|:t|		:t		same as ":copy"
|:tNext|	:tN[ext]	jump to previous matching tag
|:tabNext|	:tabN[ext]	go to previous tab page
|:tabclose|	:tabc[lose]	close current tab page
|:tabdo|	:tabdo		execute command in each tab page
|:tabedit|	:tabe[dit]	edit a file in a new tab page
|:tabfind|	:tabf[ind]	find file in 'path', edit it in a new tab page
|:tabfirst|	:tabfir[st]	go to first tab page
|:tablast|	:tabl[ast]	go to last tab page
|:tabmove|	:tabm[ove]	move tab page to other position
|:tabnew|	:tabnew		edit a file in a new tab page
|:tabnext|	:tabn[ext]	go to next tab page
|:tabonly|	:tabo[nly]	close all tab pages except the current one
|:tabprevious|	:tabp[revious]	go to previous tab page
|:tabrewind|	:tabr[ewind]	go to first tab page
|:tabs|		:tabs		list the tab pages and what they contain
|:tab|		:tab		create new tab when opening new window
|:tag|		:ta[g]		jump to tag
|:tags|		:tags		show the contents of the tag stack
|:tcd|		:tc[d]		change directory for tab page
|:tchdir|	:tch[dir]	change directory for tab page
|:terminal|	:te[rminal]	open a terminal buffer
|:tfirst|	:tf[irst]	jump to first matching tag
|:throw|	:th[row]	throw an exception
|:tjump|	:tj[ump]	like ":tselect", but jump directly when there is only one match
|:tlast|	:tl[ast]	jump to last matching tag
|:tlmenu|	:tlm[enu]	add menu for |Terminal-mode|
|:tlnoremenu|	:tln[oremenu]	like ":noremenu" but for |Terminal-mode|
|:tlunmenu|	:tlu[nmenu]	remove menu for |Terminal-mode|
|:tmapclear|	:tmapc[lear]	remove all mappings for |Terminal-mode|
|:tmap|		:tma[p]		like ":map" but for |Terminal-mode|
|:tmenu|	:tm[enu]	define menu tooltip
|:tnext|	:tn[ext]	jump to next matching tag
|:tnoremap|	:tno[remap]	like ":noremap" but for |Terminal-mode|
|:topleft|	:to[pleft]	make split window appear at top or far left
|:tprevious|	:tp[revious]	jump to previous matching tag
|:trewind|	:tr[ewind]	jump to first matching tag
|:trust|	:trust		add or remove file from trust database
|:try|		:try		execute commands, abort on error or exception
|:tselect|	:ts[elect]	list matching tags and select one
|:tunmap|	:tunma[p]	like ":unmap" but for |Terminal-mode|
|:tunmenu|	:tu[nmenu]	remove menu tooltip
|:undo|		:u[ndo]		undo last change(s)
|:undojoin|	:undoj[oin]	join next change with previous undo block
|:undolist|	:undol[ist]	list leafs of the undo tree
|:unabbreviate|	:una[bbreviate]	remove abbreviation
|:unhide|	:unh[ide]	open a window for each loaded file in the buffer list
|:unlet|	:unl[et]	delete variable
|:unlockvar|	:unlo[ckvar]	unlock variables
|:unmap|	:unm[ap]	remove mapping
|:unmenu|	:unme[nu]	remove menu
|:unsilent|	:uns[ilent]	run a command not silently
|:update|	:up[date]	write buffer if modified
|:vglobal|	:v[global]	execute commands for not matching lines
|:version|	:ve[rsion]	print version number and other info
|:verbose|	:verb[ose]	execute command with 'verbose' set
|:vertical|	:vert[ical]	make following command split vertically
|:vimgrep|	:vim[grep]	search for pattern in files
|:vimgrepadd|	:vimgrepa[dd]	like :vimgrep, but append to current list
|:visual|	:vi[sual]	same as ":edit", but turns off "Ex" mode
|:viusage|	:viu[sage]	overview of Normal mode commands
|:view|		:vie[w]		edit a file read-only
|:vmap|		:vm[ap]		like ":map" but for Visual+Select mode
|:vmapclear|	:vmapc[lear]	remove all mappings for Visual+Select mode
|:vmenu|	:vme[nu]	add menu for Visual+Select mode
|:vnew|		:vne[w]		create a new empty window, vertically split
|:vnoremap|	:vn[oremap]	like ":noremap" but for Visual+Select mode
|:vnoremenu|	:vnoreme[nu]	like ":noremenu" but for Visual+Select mode
|:vsplit|	:vs[plit]	split current window vertically
|:vunmap|	:vu[nmap]	like ":unmap" but for Visual+Select mode
|:vunmenu|	:vunme[nu]	remove menu for Visual+Select mode
|:windo|	:windo		execute command in each window
|:write|	:w[rite]	write to a file
|:wNext|	:wN[ext]	write to a file and go to previous file in argument list
|:wall|		:wa[ll]		write all (changed) buffers
|:while|	:wh[ile]	execute loop for as long as condition met
|:winsize|	:wi[nsize]	get or set window size (obsolete)
|:wincmd|	:winc[md]	execute a Window (CTRL-W) command
|:winpos|	:winp[os]	get or set window position
|:wnext|	:wn[ext]	write to a file and go to next file in argument list
|:wprevious|	:wp[revious]	write to a file and go to previous file in argument list
|:wq|		:wq		write to a file and quit window or Vim
|:wqall|	:wqa[ll]	write all changed buffers and quit Vim
|:wshada|	:wsh[ada]	write to ShaDa file
|:wundo|	:wu[ndo]	write undo information to a file
|:xit|		:x[it]		write if buffer changed and close window
|:xall|		:xa[ll]		same as ":wqall"
|:xmapclear|	:xmapc[lear]	remove all mappings for Visual mode
|:xmap|		:xm[ap]		like ":map" but for Visual mode
|:xmenu|	:xme[nu]	add menu for Visual mode
|:xnoremap|	:xn[oremap]	like ":noremap" but for Visual mode
|:xnoremenu|	:xnoreme[nu]	like ":noremenu" but for Visual mode
|:xunmap|	:xu[nmap]	like ":unmap" but for Visual mode
|:xunmenu|	:xunme[nu]	remove menu for Visual mode
|:yank|		:y[ank]		yank lines into a register
|:z|		:z		print some lines
|:~|		:~		repeat last ":substitute"
Left-right motion |h|	N  h		left (also: CTRL-H, <BS>, or <Left> key)
Left-right motion |l|	N  l		right (also: <Space> or <Right> key)
Left-right motion |0|	   0		to first character in the line (also: <Home> key)
Left-right motion |^|	   ^		to first non-blank character in the line
Left-right motion |$|	N  $		to the next EOL (end of line) position (also: <End> key)
Left-right motion |g0|	   g0		to first character in screen line (differs from "0" when lines wrap)
Left-right motion |g^|	   g^		to first non-blank character in screen line (differs from "^" when lines wrap)
Left-right motion |g$|	N  g$		to last character in screen line (differs from "$" when lines wrap)
Left-right motion |gm|	   gm		to middle of the screen line
Left-right motion |gM|	   gM		to middle of the line
Left-right motion |bar|	N  |		to column N (default: 1)
Left-right motion |f|	N  f{char}	to the Nth occurrence of {char} to the right
Left-right motion |F|	N  F{char}	to the Nth occurrence of {char} to the left
Left-right motion |t|	N  t{char}	till before the Nth occurrence of {char} to the right
Left-right motion |T|	N  T{char}	till before the Nth occurrence of {char} to the left
Left-right motion |;|	N  ;		repeat the last "f", "F", "t", or "T" N times
Left-right motion |,|	N  ,		repeat the last "f", "F", "t", or "T" N times in opposite direction
Up-down motion |k|	N  k		up N lines (also: CTRL-P and <Up>)
Up-down motion |j|	N  j		down N lines (also: CTRL-J, CTRL-N, <NL>, and <Down>)
Up-down motion |-|	N  -		up N lines, on the first non-blank character
Up-down motion |+|	N  +		down N lines, on the first non-blank character (also: CTRL-M and <CR>)
Up-down motion |_|	N  _		down N-1 lines, on the first non-blank character
Up-down motion |G|	N  G		goto line N (default: last line), on the first non-blank character
Up-down motion |gg|	N  gg		goto line N (default: first line), on the first non-blank character
Up-down motion |N%|	N  %		goto line N percentage down in the file; N must be given, otherwise it is the |%| command
Up-down motion |gk|	N  gk		up N screen lines (differs from "k" when line wraps)
Up-down motion |gj|	N  gj		down N screen lines (differs from "j" when line wraps)
Text object |w|	N  w		N words forward
Text object |W|	N  W		N blank-separated |WORD|s forward
Text object |e|	N  e		forward to the end of the Nth word
Text object |E|	N  E		forward to the end of the Nth blank-separated |WORD|
Text object |b|	N  b		N words backward
Text object |B|	N  B		N blank-separated |WORD|s backward
Text object |ge|	N  ge		backward to the end of the Nth word
Text object |gE|	N  gE		backward to the end of the Nth blank-separated |WORD|
Text object |)|	N  )		N sentences forward
Text object |(|	N  (		N sentences backward
Text object |}|	N  }		N paragraphs forward
Text object |{|	N  {		N paragraphs backward
Text object |]]|	N  ]]		N sections forward, at start of section
Text object |[[|	N  [[		N sections backward, at start of section
Text object |][|	N  ][		N sections forward, at end of section
Text object |[]|	N  []		N sections backward, at end of section
Text object |[(|	N  [(		N times back to unclosed '('
Text object |[{|	N  [{		N times back to unclosed '{'
Text object |[m|	N  [m		N times back to start of method (for Java)
Text object |[M|	N  [M		N times back to end of method (for Java)
Text object |])|	N  ])		N times forward to unclosed ')'
Text object |]}|	N  ]}		N times forward to unclosed '}'
Text object |]m|	N  ]m		N times forward to start of method (for Java)
Text object |]M|	N  ]M		N times forward to end of method (for Java)
Text object |[#|	N  [#		N times back to unclosed "#if" or "#else"
Text object |]#|	N  ]#		N times forward to unclosed "#else" or "#endif"
Text object |[star|	N  [*		N times back to start of comment "/*"
Text object |]star|	N  ]*		N times forward to end of comment "*/"
Search: |/|	N  /{pattern}[/[offset]]<CR> search forward for the Nth occurrence of {pattern}
Search: |?|	N  ?{pattern}[?[offset]]<CR> search backward for the Nth occurrence of {pattern}
Search: |/<CR>|	N  /<CR>	repeat last search, in the forward direction
Search: |?<CR>|	N  ?<CR>	repeat last search, in the backward direction
Search: |n|	N  n		repeat last search
Search: |N|	N  N		repeat last search, in opposite direction
Search: |star|	N  *		search forward for the identifier under the cursor
Search: |#|	N  #		search backward for the identifier under the cursor
Search: |gstar|	N  g*		like "*", but also find partial matches
Search: |g#|	N  g#		like "#", but also find partial matches
Search: |gd|	   gd		goto local declaration of identifier under the cursor
Search: |gD|	   gD		goto global declaration of identifier under the cursor
Search: matches any single character	.	\.
Search: matches start of line	^	^
Search: matches <EOL>	$	$
Search: matches start of word	\<	\<
Search: matches end of word	\>	\>
Search: matches a single char from the range	[a-z]	\[a-z]
Search: matches a single char not in the range	[^a-z]	\[^a-z]
Search: matches an identifier char	\i	\i
Search: matches an identifier char but excluding digits	\I	\I
Search: matches a keyword character	\k	\k
Search: matches a keyword character but excluding digits	\K	\K
Search: matches a file name character	\f	\f
Search: matches a file name character but excluding digits	\F	\F
Search: matches a printable character	\p	\p
Search: matches a printable characte but excluding digits	\P	\P
Search: matches a white space character	\s	\s
Search: matches a non-white space character	\S	\S
Search: matches <Esc>	\e	\e
Search: matches <Tab>	\t	\t
Search: matches <CR>	\r	\r
Search: matches <BS>	\b	\b
Search: matches 0 or more of the preceding atom	*	\*
Search: matches 1 or more of the preceding atom	\+	\+
Search: matches 0 or 1 of the preceding atom	\=	\=
Search: matches 2 to 5 of the preceding atom	\{2,5}  \{2,5}
Search: separates two alternatives	\|	\|
Search: group a pattern into an atom	\(\)	\(\)
Search offset: [num]	[num] lines downwards, in column 1
Search offset: +[num]	[num] lines downwards, in column 1
Search offset: -[num]	[num] lines upwards, in column 1
Search offset: e[+num]	[num] characters to the right of the end of the match
Search offset: e[-num]	[num] characters to the left of the end of the match
Search offset: s[+num]	[num] characters to the right of the start of the match
Search offset: s[-num]	[num] characters to the left of the start of the match
Search offset: b[+num]	[num] identical to s[+num] above (mnemonic: begin)
Search offset: b[-num]	[num] identical to s[-num] above (mnemonic: begin)
Search offset: ;{search-command}	execute {search-command} next
Mark: |m|        m{a-zA-Z}	mark current position with mark {a-zA-Z}
Mark: |`a|       `{a-z}	go to mark {a-z} within current file
Mark: |`A|       `{A-Z}	go to mark {A-Z} in any file
Mark: |`0|       `{0-9}	go to the position where Vim was previously exited
Mark: |``|       ``		go to the position before the last jump
Mark: |`quote|   `"		go to the position when last editing this file
Mark: |`[|       `[		go to the start of the previously operated or put text
Mark: |`]|       `]		go to the end of the previously operated or put text
Mark: |`<|       `<		go to the start of the (previous) Visual area
Mark: |`>|       `>		go to the end of the (previous) Visual area
Mark: |`.|       `.		go to the position of the last change in this file
Mark: |'|        '{a-zA-Z0-9[]'"<>.} same as `, but on the first non-blank in the line
Mark: |:marks|  :marks	print the active marks
Mark: |CTRL-O|  N  CTRL-O	go to Nth older position in jump list
Mark: |CTRL-I|  N  CTRL-I	go to Nth newer position in jump list
Mark: |:ju|     :ju[mps]	print the jump list
|%|	   %		find the next brace, bracket, comment, or "#if"/ "#else"/"#endif" in this line and go to its match
|H|	N  H		go to the Nth line in the window, on the first non-blank
|M|	   M		go to the middle line in the window, on the first non-blank
|L|	N  L		go to the Nth line from the bottom, on the first non-blank
|go|	N  go			go to Nth byte in the buffer
|:go|	:[range]go[to] [off]	go to [off] byte in the buffer
|:ta|      :ta[g][!] {tag}	jump to tag {tag}
|:ta|      :[count]ta[g][!]	jump to [count]'th newer tag in tag list
|CTRL-]|      CTRL-]		jump to the tag under cursor, unless changes have been made
|:ts|      :ts[elect][!] [tag]	list matching tags and select one to jump to
|:tjump|   :tj[ump][!] [tag]	jump to tag [tag] or select from list when there are multiple matches
|:ltag|    :lt[ag][!] [tag]	jump to tag [tag] and add matching tags to the location list
|:tags|    :tags		print tag list
|CTRL-T|   N  CTRL-T		jump back from Nth older tag in tag list
|:po|      :[count]po[p][!]	jump back from [count]'th older tag in tag list
|:tnext|   :[count]tn[ext][!]	jump to [count]'th next matching tag
|:tp|      :[count]tp[revious][!] jump to [count]'th previous matching tag
|:tr|      :[count]tr[ewind][!]	jump to [count]'th matching tag
|:tl|      :tl[ast][!]		jump to last matching tag
|:ptag|    :pt[ag] {tag}	open a preview window to show tag {tag}
|CTRL-W_}|    CTRL-W }		like CTRL-] but show tag in preview window
|:pts|     :pts[elect]		like ":tselect" but show tag in preview window
|:ptjump|  :ptj[ump]		like ":tjump" but show tag in preview window
|:pclose|  :pc[lose]		close tag preview window
|CTRL-W_z|    CTRL-W z		close tag preview window
|CTRL-E|	N  CTRL-E	window N lines downwards (default: 1)
|CTRL-D|	N  CTRL-D	window N lines Downwards (default: 1/2 window)
|CTRL-F|	N  CTRL-F	window N pages Forwards (downwards)
|CTRL-Y|	N  CTRL-Y	window N lines upwards (default: 1)
|CTRL-U|	N  CTRL-U	window N lines Upwards (default: 1/2 window)
|CTRL-B|	N  CTRL-B	window N pages Backwards (upwards)
|z<CR>|		   z<CR> or zt	redraw, current line at top of window
|z.|		   z.	 or zz	redraw, current line at center of window
|z-|		   z-	 or zb	redraw, current line at bottom of window
|zh|		N  zh		scroll screen N characters to the right, wrap off
|zl|		N  zl		scroll screen N characters to the left, wrap off
|zH|		N  zH		scroll screen half a screenwidth to the right, wrap off
|zL|		N  zL		scroll screen half a screenwidth to the left, wrap off
|a|	N  a	append text after the cursor (N times)
|A|	N  A	append text at the end of the line (N times)
|i|	N  i	insert text before the cursor (N times) (also: <Insert>)
|I|	N  I	insert text before the first non-blank in the line (N times)
|gI|	N  gI	insert text in column 1 (N times)
|o|	N  o	open a new line below the current line, append text (N times)
|O|	N  O	open a new line above the current line, append text (N times)
|:startinsert|  :star[tinsert][!]  start Insert mode, append when [!] used
|:startreplace| :startr[eplace][!]  start Replace mode, at EOL when [!] used
Visual block: |v_b_I|	   I	insert the same text in front of all the selected lines
Visual block: |v_b_A|	   A	append the same text after all the selected lines
|i_<Esc>|	<Esc>		  end Insert mode, back to Normal mode
|i_CTRL-C|	CTRL-C		  like <Esc>, but do not use an abbreviation
|i_CTRL-O|	CTRL-O {command}  execute {command} and return to Insert mode
|i_<Up>|	cursor keys	  move cursor left/right/up/down
|i_<S-Left>|	shift-left/right  one word left/right
|i_<S-Up>|	shift-up/down	  one screenful backward/forward
|i_<End>|	<End>		  cursor after last character in the line
|i_<Home>|	<Home>		  cursor to first character in the line
|i_CTRL-V|	CTRL-V {char}..	  insert character literally, or enter decimal byte value
|i_<NL>|	<NL> or <CR> or CTRL-M or CTRL-J begin new line
|i_CTRL-E|	CTRL-E		  insert the character from below the cursor
|i_CTRL-Y|	CTRL-Y		  insert the character from above the cursor
|i_CTRL-A|	CTRL-A		  insert previously inserted text
|i_CTRL-@|	CTRL-@		  insert previously inserted text and stop Insert mode
|i_CTRL-R|	CTRL-R {register} insert the contents of a register
|i_CTRL-N|	CTRL-N		  insert next match of identifier before the cursor
|i_CTRL-P|	CTRL-P		  insert previous match of identifier before the cursor
|i_CTRL-X|	CTRL-X ...	  complete the word before the cursor in various ways
|i_<BS>|	<BS> or CTRL-H	  delete the character before the cursor
|i_<Del>|	<Del>		  delete the character under the cursor
|i_CTRL-W|	CTRL-W		  delete word before the cursor
|i_CTRL-U|	CTRL-U		  delete all entered characters in the current line
|i_CTRL-T|	CTRL-T		  insert one shiftwidth of indent in front of the current line
|i_CTRL-D|	CTRL-D		  delete one shiftwidth of indent in front of the current line
|i_0_CTRL-D|	0 CTRL-D	  delete all indent in the current line
|i_^_CTRL-D|	^ CTRL-D	  delete all indent in the current line, restore indent in next line
|:dig|	   :dig[raphs]		show current list of digraphs
|:dig|	   :dig[raphs] {char1}{char2} {number} ... add digraph(s) to the list
|i_CTRL-K|	CTRL-K {char1} {char2} enter digraph
|i_digraph|	{char1} <BS> {char2} enter digraph if 'digraph' option set
|:r|	   :r [file]	   insert the contents of [file] below the cursor
|:r!|	   :r! {command}   insert the standard output of {command} below the cursor
|x|	N  x		delete N characters under and after the cursor
|<Del>|	N  <Del>	delete N characters under and after the cursor
|X|	N  X		delete N characters before the cursor
|d|	N  d{motion}	delete the text that is moved over with {motion}
|v_d|	   {visual}d	delete the highlighted text
|dd|	N  dd		delete N lines
|D|	N  D		delete to the end of the line (and N-1 more lines)
|J|	N  J		join N-1 lines (delete <EOL>s)
|v_J|	   {visual}J	join the highlighted lines
|gJ|	N  gJ		like "J", but without inserting spaces
|v_gJ|	   {visual}gJ	like "{visual}J", but without inserting spaces
|:d|	:[range]d [x]	delete [range] lines [into register x]
|quote|	  "{char}	use register {char} for the next delete, yank, or put
|:reg|	  :reg		show the contents of all registers
|:reg|	  :reg {arg}	show the contents of registers mentioned in {arg}
|y|	  N  y{motion}	yank the text moved over with {motion} into a register
|v_y|	     {visual}y	yank the highlighted text into a register
|yy|	  N  yy		yank N lines into a register
|Y|	  N  Y		yank N lines into a register. Mapped to "y$" by default.
|p|	  N  p		put a register after the cursor position (N times)
|P|	  N  P		put a register before the cursor position (N times)
|]p|	  N  ]p		like p, but adjust indent to current line
|[p|	  N  [p		like P, but adjust indent to current line
|gp|	  N  gp		like p, but leave cursor after the new text
|gP|	  N  gP		like P, but leave cursor after the new text
|r|	  N  r{char}	replace N characters with {char}
|gr|	  N  gr{char}	replace N characters without affecting layout
|R|	  N  R		enter Replace mode (repeat the entered text N times)
|gR|	  N  gR		enter virtual Replace mode: Like Replace mode but without affecting layout
|v_b_r|	     {visual}r{char} in Visual block mode: Replace each char of the selected text with {char}
|c|	  N  c{motion}	change the text that is moved over with {motion}
|v_c|	     {visual}c	change the highlighted text
|cc|	  N  cc		change N lines
|S|	  N  S		change N lines
|C|	  N  C		change to the end of the line (and N-1 more lines)
|s|	  N  s		change N characters
|v_b_c|	     {visual}c	in Visual block mode: Change each of the selected lines with the entered text
|v_b_C|	     {visual}C	in Visual block mode: Change each of the selected lines until end-of-line with the entered text
|~|	  N  ~		switch case for N characters and advance cursor
|v_~|	     {visual}~	switch case for highlighted text
|v_u|	     {visual}u	make highlighted text lowercase
|v_U|	     {visual}U	make highlighted text uppercase
|g~|	     g~{motion} switch case for the text that is moved over with {motion}
|gu|	     gu{motion} make the text that is moved over with {motion} lowercase
|gU|	     gU{motion} make the text that is moved over with {motion} uppercase
|v_g?|	     {visual}g? perform rot13 encoding on highlighted text
|g?|	     g?{motion} perform rot13 encoding on the text that is moved over with {motion}
|CTRL-A|  N  CTRL-A	add N to the number at or after the cursor
|CTRL-X|  N  CTRL-X	subtract N from the number at or after the cursor
|<|	  N  <{motion}	move the lines that are moved over with {motion} one shiftwidth left
|<<|	  N  <<		move N lines one shiftwidth left
|>|	  N  >{motion}	move the lines that are moved over with {motion} one shiftwidth right
|>>|	  N  >>		move N lines one shiftwidth right
|gq|	  N  gq{motion}	format the lines that are moved over with {motion} to 'textwidth' length
|:ce|	  :[range]ce[nter] [width] center the lines in [range]
|:le|	  :[range]le[ft] [indent] left-align the lines in [range] (with [indent])
|:ri|	  :[range]ri[ght] [width] right-align the lines in [range]
|!|	   N  !{motion}{command}<CR> filter the lines that are moved over through {command}
|!!|	   N  !!{command}<CR> filter N lines through {command}
|v_!|	      {visual}!{command}<CR> filter the highlighted lines through {command}
|:range!|  :[range]! {command}<CR> filter [range] lines through {command}
|=|	   N  ={motion} filter the lines that are moved over through 'equalprg'
|==|	   N  ==	filter N lines through 'equalprg'
|v_=|	      {visual}= filter the highlighted lines through 'equalprg'
|:s|	   :[range]s[ubstitute]/{pattern}/{string}/[g][c] substitute {pattern} by {string} in [range] lines; with [g], replace all occurrences of {pattern}; with [c], confirm each replacement
|:s|	   :[range]s[ubstitute] [g][c] repeat previous ":s" with new range and options
|&|	      &		Repeat previous ":s" on current line without options
|:ret|	   :[range]ret[ab][!] [tabstop] set 'tabstop' to new value and adjust white space accordingly
|v|        v		start highlighting characters  }  move cursor and use
|V|        V		start highlighting linewise    }  operator to affect
|CTRL-V|   CTRL-V	start highlighting blockwise   }  highlighted text
|v_o|      o		exchange cursor position with start of highlighting
|gv|       gv		start highlighting on previous visual area
|v_v|      v		highlight characters or stop highlighting
|v_V|      V		highlight linewise or stop highlighting
|v_CTRL-V| CTRL-V	highlight blockwise or stop highlighting
Text object: |v_aw|	   N  aw	Select "a word"
Text object: |v_iw|	   N  iw	Select "inner word"
Text object: |v_aW|	   N  aW	Select "a |WORD|"
Text object: |v_iW|	   N  iW	Select "inner |WORD|"
Text object: |v_as|	   N  as	Select "a sentence"
Text object: |v_is|	   N  is	Select "inner sentence"
Text object: |v_ap|	   N  ap	Select "a paragraph"
Text object: |v_ip|	   N  ip	Select "inner paragraph"
Text object: |v_ab|	   N  ab	Select "a block" (from "[(" to "])")
Text object: |v_ib|	   N  ib	Select "inner block" (from "[(" to "])")
Text object: |v_aB|	   N  aB	Select "a Block" (from "[{" to "]}")
Text object: |v_iB|	   N  iB	Select "inner Block" (from "[{" to "]}")
Text object: |v_a>|	   N  a>	Select "a <> block"
Text object: |v_i>|	   N  i>	Select "inner <> block"
Text object: |v_at|	   N  at	Select "a tag block" (from <aaa> to </aaa>)
Text object: |v_it|	   N  it	Select "inner tag block" (from <aaa> to </aaa>)
Text object: |v_a'|	   N  a'	Select "a single quoted string"
Text object: |v_i'|	   N  i'	Select "inner single quoted string"
Text object: |v_aquote| N  a"	Select "a double quoted string"
Text object: |v_iquote| N  i"	Select "inner double quoted string"
Text object: |v_a`|	   N  a`	Select "a backward quoted string"
Text object: |v_i`|	   N  i`	Select "inner backward quoted string"
|.|	   N  .		repeat last change (with count replaced with N)
|q|	      q{a-z}	record typed characters into register {a-z}
|q|	      q{A-Z}	record typed characters, appended to register {a-z}
|q|	      q		stop recording
|Q|	      Q		replay last recorded macro
|@|	   N  @{a-z}	execute the contents of register {a-z} (N times)
|@@|	   N  @@	   repeat previous @{a-z} (N times)
|:@|	   :@{a-z}	execute the contents of register {a-z} as an Ex command
|:@@|	   :@@		repeat previous :@{a-z}
|:g|	   :[range]g[lobal]/{pattern}/[cmd] execute Ex command [cmd] (default: ":p") on the lines within [range] where {pattern} matches
|:g|	   :[range]g[lobal]!/{pattern}/[cmd] execute Ex command [cmd] (default: ":p") on the lines within [range] where {pattern} does NOT match
|:so|	   :so[urce] {file} read Ex commands from {file}
|:so|	   :so[urce]! {file} read Vim commands from {file}
|:sl|	   :sl[eep] [sec] don't do anything for [sec] seconds
|gs|	   N  gs	goto Sleep for N seconds
|:map|       :ma[p] {lhs} {rhs}	  map {lhs} to {rhs} in Normal and Visual mode
|:map!|      :ma[p]! {lhs} {rhs}  map {lhs} to {rhs} in Insert and Command-line mode
|:noremap|   :no[remap][!] {lhs} {rhs} same as ":map", no remapping for this {rhs}
|:unmap|     :unm[ap] {lhs}	  remove the mapping of {lhs} for Normal and Visual mode
|:unmap!|    :unm[ap]! {lhs}	  remove the mapping of {lhs} for Insert and Command-line mode
|:map_l|     :ma[p] [lhs]	  list mappings (starting with [lhs]) for Normal and Visual mode
|:map_l!|    :ma[p]! [lhs]	  list mappings (starting with [lhs]) for Insert and Command-line mode
|:cmap|      :cmap/:cunmap/:cnoremap like ":map!"/":unmap!"/":noremap!" but for Command-line mode only
|:imap|      :imap/:iunmap/:inoremap like ":map!"/":unmap!"/":noremap!" but for Insert mode only
|:nmap|      :nmap/:nunmap/:nnoremap like ":map"/":unmap"/":noremap" but for Normal mode only
|:vmap|      :vmap/:vunmap/:vnoremap like ":map"/":unmap"/":noremap" but for Visual mode only
|:omap|      :omap/:ounmap/:onoremap like ":map"/":unmap"/":noremap" but only for when an operator is pending
|:mapc|      :mapc[lear]	  remove mappings for Normal and Visual mode
|:mapc|      :mapc[lear]!	  remove mappings for Insert and Cmdline mode
|:imapc|     :imapc[lear]	  remove mappings for Insert mode
|:vmapc|     :vmapc[lear]	  remove mappings for Visual mode
|:omapc|     :omapc[lear]	  remove mappings for Operator-pending mode
|:nmapc|     :nmapc[lear]	  remove mappings for Normal mode
|:cmapc|     :cmapc[lear]	  remove mappings for Cmdline mode
|:mkexrc|    :mk[exrc][!] [file]  write current mappings, abbreviations, and settings to [file] (default: ".exrc"; use ! to overwrite)
|:mkvimrc|   :mkv[imrc][!] [file] same as :mkexrc, but with default ".nvimrc"
|:mksession| :mks[ession][!] [file] like ":mkvimrc", but store current files, windows, etc. too, to be able to continue this session later
|:abbreviate|	:ab[breviate] {lhs} {rhs}  add abbreviation for {lhs} to {rhs}
|:abbreviate|	:ab[breviate] {lhs}	   show abbr's that start with {lhs}
|:abbreviate|	:ab[breviate]		   show all abbreviations
|:unabbreviate|	:una[bbreviate] {lhs}	   remove abbreviation for {lhs}
|:noreabbrev|	:norea[bbrev] [lhs] [rhs]  like ":ab", but don't remap [rhs]
|:iabbrev|	:iab/:iunab/:inoreab	   like ":ab", but only for Insert mode
|:cabbrev|	:cab/:cunab/:cnoreab	   like ":ab", but only for Command-line mode
|:abclear|	:abc[lear]		   remove all abbreviations
|:cabclear|	:cabc[lear]		   remove all abbr's for Cmdline mode
|:iabclear|	:iabc[lear]		   remove all abbr's for Insert mode
|:set|		:se[t]			  show all modified options
|:set|		:se[t] all		  show all options
|:set|		:se[t] {option}		  set boolean option (switch it on), show string or number option
|:set|		:se[t] no{option}	  reset boolean option (switch it off)
|:set|		:se[t] inv{option}	  invert boolean option
|:set|		:se[t] {option}={value}	  set string/number option to {value}
|:set|		:se[t] {option}+={value}  append {value} to string option, add {value} to number option
|:set|		:se[t] {option}-={value}  remove {value} to string option, subtract {value} from number option
|:set|		:se[t] {option}?	  show value of {option}
|:set|		:se[t] {option}&	  reset {option} to its default value
|:setlocal|	:setl[ocal]		  like ":set" but set the local value for options that have one
|:setglobal|	:setg[lobal]		  like ":set" but set the global value of a local option
|:options|	:opt[ions]		  open a new window to view and set options, grouped by functionality, a one line explanation and links to the help
Option: 'aleph'		  'al'	    ASCII code of the letter Aleph (Hebrew)
Option: 'allowrevins'	  'ari'     allow CTRL-_ in Insert and Command-line mode
Option: 'ambiwidth'	  'ambw'    what to do with Unicode chars of ambiguous width
Option: 'autochdir'	  'acd'     change directory to the file in the current window
Option: 'arabic'	  'arab'    for Arabic as a default second language
Option: 'arabicshape'	  'arshape' do shaping for Arabic characters
Option: 'autoindent'	  'ai'	    take indent for new line from previous line
Option: 'autoread'	  'ar'	    autom. read file when changed outside of Vim
Option: 'autowrite'	  'aw'	    automatically write file if changed
Option: 'autowriteall'	  'awa'     as 'autowrite', but works with more commands
Option: 'background'	  'bg'	    "dark" or "light", used for highlight colors
Option: 'backspace'	  'bs'	    how backspace works at start of line
Option: 'backup'	  'bk'	    keep backup file after overwriting a file
Option: 'backupcopy'	  'bkc'     make backup as a copy, don't rename the file
Option: 'backupdir'	  'bdir'    list of directories for the backup file
Option: 'backupext'	  'bex'     extension used for the backup file
Option: 'backupskip'	  'bsk'     no backup for files that match these patterns
Option: 'belloff'	  'bo'	    do not ring the bell for these reasons
Option: 'binary'	  'bin'     read/write/edit file in binary mode
Option: 'bomb'			    prepend a Byte Order Mark to the file
Option: 'breakat'	  'brk'     characters that may cause a line break
Option: 'breakindent'	  'bri'     wrapped line repeats indent
Option: 'breakindentopt'  'briopt'  settings for 'breakindent'
Option: 'browsedir'	  'bsdir'   which directory to start browsing in
Option: 'bufhidden'	  'bh'	    what to do when buffer is no longer in window
Option: 'buflisted'	  'bl'	    whether the buffer shows up in the buffer list
Option: 'buftype'	  'bt'	    special type of buffer
Option: 'casemap'	  'cmp'     specifies how case of letters is changed
Option: 'cdhome'	  'cdh'	    change directory to the home directory by ":cd"
Option: 'cdpath'	  'cd'	    list of directories searched with ":cd"
Option: 'cedit'			    key used to open the command-line window
Option: 'charconvert'	  'ccv'     expression for character encoding conversion
Option: 'cindent'	  'cin'     do C program indenting
Option: 'cinkeys'	  'cink'    keys that trigger indent when 'cindent' is set
Option: 'cinoptions'	  'cino'    how to do indenting when 'cindent' is set
Option: 'cinwords'	  'cinw'    words where 'si' and 'cin' add an indent
Option: 'cinscopedecls'	  'cinsd'   words that are recognized by 'cino-g'
Option: 'clipboard'	  'cb'	    use the clipboard as the unnamed register
Option: 'cmdheight'	  'ch'	    number of lines to use for the command-line
Option: 'cmdwinheight'	  'cwh'     height of the command-line window
Option: 'colorcolumn'	  'cc'	    columns to highlight
Option: 'columns'	  'co'	    number of columns in the display
Option: 'comments'	  'com'     patterns that can start a comment line
Option: 'commentstring'   'cms'     template for comments; used for fold marker
Option: 'complete'	  'cpt'     specify how Insert mode completion works
Option: 'completefunc'	  'cfu'     function to be used for Insert mode completion
Option: 'completeopt'	  'cot'     options for Insert mode completion
Option: 'completeslash'	  'csl'	    like 'shellslash' for completion
Option: 'concealcursor'	  'cocu'    whether concealable text is hidden in cursor line
Option: 'conceallevel'	  'cole'    whether concealable text is shown or hidden
Option: 'confirm'	  'cf'	    ask what to do about unsaved/read-only files
Option: 'copyindent'	  'ci'	    make 'autoindent' use existing indent structure
Option: 'cpoptions'	  'cpo'     flags for Vi-compatible behavior
Option: 'cursorbind'	  'crb'     move cursor in window as it moves in other windows
Option: 'cursorcolumn'	  'cuc'	    highlight the screen column of the cursor
Option: 'cursorline'	  'cul'	    highlight the screen line of the cursor
Option: 'cursorlineopt'	  'culopt'  settings for 'cursorline'
Option: 'debug'			    set to "msg" to see all error messages
Option: 'define'	  'def'     pattern to be used to find a macro definition
Option: 'delcombine'	  'deco'    delete combining characters on their own
Option: 'dictionary'	  'dict'    list of file names used for keyword completion
Option: 'diff'			    use diff mode for the current window
Option: 'diffexpr'	  'dex'     expression used to obtain a diff file
Option: 'diffopt'	  'dip'     options for using diff mode
Option: 'digraph'	  'dg'	    enable the entering of digraphs in Insert mode
Option: 'directory'	  'dir'     list of directory names for the swap file
Option: 'display'	  'dy'	    list of flags for how to display text
Option: 'eadirection'	  'ead'     in which direction 'equalalways' works
Option: 'encoding'	  'enc'     encoding used internally
Option: 'endoffile'	  'eof'     write CTRL-Z at end of the file
Option: 'endofline'	  'eol'     write <EOL> for last line in file
Option: 'equalalways'	  'ea'	    windows are automatically made the same size
Option: 'equalprg'	  'ep'	    external program to use for "=" command
Option: 'errorbells'	  'eb'	    ring the bell for error messages
Option: 'errorfile'	  'ef'	    name of the errorfile for the QuickFix mode
Option: 'errorformat'	  'efm'     description of the lines in the error file
Option: 'eventignore'	  'ei'	    autocommand events that are ignored
Option: 'expandtab'	  'et'	    use spaces when <Tab> is inserted
Option: 'exrc'		  'ex'	    read init files in the current directory
Option: 'fileencoding'	  'fenc'    file encoding for multibyte text
Option: 'fileencodings'   'fencs'   automatically detected character encodings
Option: 'fileformat'	  'ff'	    file format used for file I/O
Option: 'fileformats'	  'ffs'     automatically detected values for 'fileformat'
Option: 'fileignorecase'  'fic'     ignore case when using file names
Option: 'filetype'	  'ft'	    type of file, used for autocommands
Option: 'fillchars'	  'fcs'     characters to use for displaying special items
Option: 'fixendofline'	  'fixeol'  make sure last line in file has <EOL>
Option: 'foldclose'	  'fcl'     close a fold when the cursor leaves it
Option: 'foldcolumn'	  'fdc'     width of the column used to indicate folds
Option: 'foldenable'	  'fen'     set to display all folds open
Option: 'foldexpr'	  'fde'     expression used when 'foldmethod' is "expr"
Option: 'foldignore'	  'fdi'     ignore lines when 'foldmethod' is "indent"
Option: 'foldlevel'	  'fdl'     close folds with a level higher than this
Option: 'foldlevelstart'  'fdls'    'foldlevel' when starting to edit a file
Option: 'foldmarker'	  'fmr'     markers used when 'foldmethod' is "marker"
Option: 'foldmethod'	  'fdm'     folding type
Option: 'foldminlines'	  'fml'     minimum number of lines for a fold to be closed
Option: 'foldnestmax'	  'fdn'     maximum fold depth
Option: 'foldopen'	  'fdo'     for which commands a fold will be opened
Option: 'foldtext'	  'fdt'     expression used to display for a closed fold
Option: 'formatexpr'	  'fex'     expression used with "gq" command
Option: 'formatlistpat'   'flp'     pattern used to recognize a list header
Option: 'formatoptions'   'fo'	    how automatic formatting is to be done
Option: 'formatprg'	  'fp'	    name of external program used with "gq" command
Option: 'fsync'		  'fs'	    whether to invoke fsync() after file write
Option: 'gdefault'	  'gd'	    the ":substitute" flag 'g' is default on
Option: 'grepformat'	  'gfm'     format of 'grepprg' output
Option: 'grepprg'	  'gp'	    program to use for ":grep"
Option: 'guicursor'	  'gcr'     GUI: settings for cursor shape and blinking
Option: 'guifont'	  'gfn'     GUI: Name(s) of font(s) to be used
Option: 'guifontwide'	  'gfw'     list of font names for double-wide characters
Option: 'guioptions'	  'go'	    GUI: Which components and options are used
Option: 'guitablabel'	  'gtl'     GUI: custom label for a tab page
Option: 'guitabtooltip'   'gtt'     GUI: custom tooltip for a tab page
Option: 'helpfile'	  'hf'	    full path name of the main help file
Option: 'helpheight'	  'hh'	    minimum height of a new help window
Option: 'helplang'	  'hlg'     preferred help languages
Option: 'hidden'	  'hid'     don't unload buffer when it is |abandon|ed
Option: 'hlsearch'	  'hls'     highlight matches with last search pattern
Option: 'history'	  'hi'	    number of command-lines that are remembered
Option: 'hkmap'		  'hk'	    Hebrew keyboard mapping
Option: 'hkmapp'	  'hkp'     phonetic Hebrew keyboard mapping
Option: 'icon'			    let Vim set the text of the window icon
Option: 'iconstring'		    string to use for the Vim icon text
Option: 'ignorecase'	  'ic'	    ignore case in search patterns
Option: 'imcmdline'	  'imc'     use IM when starting to edit a command line
Option: 'imdisable'	  'imd'     do not use the IM in any mode
Option: 'iminsert'	  'imi'     use :lmap or IM in Insert mode
Option: 'imsearch'	  'ims'     use :lmap or IM when typing a search pattern
Option: 'include'	  'inc'     pattern to be used to find an include file
Option: 'includeexpr'	  'inex'    expression used to process an include line
Option: 'incsearch'	  'is'	    highlight match while typing search pattern
Option: 'indentexpr'	  'inde'    expression used to obtain the indent of a line
Option: 'indentkeys'	  'indk'    keys that trigger indenting with 'indentexpr'
Option: 'infercase'	  'inf'     adjust case of match for keyword completion
Option: 'isfname'	  'isf'     characters included in file names and pathnames
Option: 'isident'	  'isi'     characters included in identifiers
Option: 'iskeyword'	  'isk'     characters included in keywords
Option: 'isprint'	  'isp'     printable characters
Option: 'joinspaces'	  'js'	    two spaces after a period with a join command
Option: 'jumpoptions'	  'jop'     specifies how jumping is done
Option: 'keymap'	  'kmp'     name of a keyboard mapping
Option: 'keymodel'	  'km'	    enable starting/stopping selection with keys
Option: 'keywordprg'	  'kp'	    program to use for the "K" command
Option: 'langmap'	  'lmap'    alphabetic characters for other language mode
Option: 'langmenu'	  'lm'	    language to be used for the menus
Option: 'langremap'	  'lrm'	    do apply 'langmap' to mapped characters
Option: 'laststatus'	  'ls'	    tells when last window has status lines
Option: 'lazyredraw'	  'lz'	    don't redraw while executing macros
Option: 'linebreak'	  'lbr'     wrap long lines at a blank
Option: 'lines'			    number of lines in the display
Option: 'linespace'	  'lsp'     number of pixel lines to use between characters
Option: 'lisp'			    automatic indenting for Lisp
Option: 'lispoptions'	  'lop'     changes how Lisp indenting is done
Option: 'lispwords'	  'lw'	    words that change how lisp indenting works
Option: 'list'			    show <Tab> and <EOL>
Option: 'listchars'	  'lcs'     characters for displaying in list mode
Option: 'loadplugins'	  'lpl'     load plugin scripts when starting up
Option: 'magic'			    changes special characters in search patterns
Option: 'makeef'	  'mef'     name of the errorfile for ":make"
Option: 'makeencoding'	  'menc'    encoding of external make/grep commands
Option: 'makeprg'	  'mp'	    program to use for the ":make" command
Option: 'matchpairs'	  'mps'     pairs of characters that "%" can match
Option: 'matchtime'	  'mat'     tenths of a second to show matching paren
Option: 'maxcombine'	  'mco'     maximum nr of combining characters displayed
Option: 'maxfuncdepth'	  'mfd'     maximum recursive depth for user functions
Option: 'maxmapdepth'	  'mmd'     maximum recursive depth for mapping
Option: 'maxmempattern'   'mmp'     maximum memory (in Kbyte) used for pattern search
Option: 'menuitems'	  'mis'     maximum number of items in a menu
Option: 'mkspellmem'	  'msm'     memory used before |:mkspell| compresses the tree
Option: 'modeline'	  'ml'	    recognize modelines at start or end of file
Option: 'modelineexpr'	  'mle'	    allow setting expression options from a modeline
Option: 'modelines'	  'mls'     number of lines checked for modelines
Option: 'modifiable'	  'ma'	    changes to the text are not possible
Option: 'modified'	  'mod'     buffer has been modified
Option: 'more'			    pause listings when the whole screen is filled
Option: 'mouse'			    enable the use of mouse clicks
Option: 'mousefocus'	  'mousef'  keyboard focus follows the mouse
Option: 'mousehide'	  'mh'	    hide mouse pointer while typing
Option: 'mousemodel'	  'mousem'  changes meaning of mouse buttons
Option: 'mousemoveevent'  'mousemev'  report mouse moves with <MouseMove>
Option: 'mousescroll'		    amount to scroll by when scrolling with a mouse
Option: 'mouseshape'	  'mouses'  shape of the mouse pointer in different modes
Option: 'mousetime'	  'mouset'  max time between mouse double-click
Option: 'nrformats'	  'nf'	    number formats recognized for CTRL-A command
Option: 'number'	  'nu'	    print the line number in front of each line
Option: 'numberwidth'	  'nuw'     number of columns used for the line number
Option: 'omnifunc'	  'ofu'     function for filetype-specific completion
Option: 'opendevice'	  'odev'    allow reading/writing devices on MS-Windows
Option: 'operatorfunc'	  'opfunc'  function to be called for |g@| operator
Option: 'packpath'	  'pp'      list of directories used for packages
Option: 'paragraphs'	  'para'    nroff macros that separate paragraphs
Option: 'patchexpr'	  'pex'     expression used to patch a file
Option: 'patchmode'	  'pm'	    keep the oldest version of a file
Option: 'path'		  'pa'	    list of directories searched with "gf" et.al.
Option: 'preserveindent'  'pi'	    preserve the indent structure when reindenting
Option: 'previewheight'   'pvh'     height of the preview window
Option: 'previewpopup'    'pvp'     use popup window for preview
Option: 'previewwindow'   'pvw'     identifies the preview window
Option: 'pumheight'	  'ph'	    maximum number of items to show in the popup menu
Option: 'pumwidth'	  'pw'	    minimum width of the popup menu
Option: 'pyxversion'	  'pyx'	    Python version used for pyx* commands
Option: 'quoteescape'	  'qe'	    escape characters used in a string
Option: 'readonly'	  'ro'	    disallow writing the buffer
Option: 'redrawtime'	  'rdt'     timeout for 'hlsearch' and |:match| highlighting
Option: 'regexpengine'	  're'	    default regexp engine to use
Option: 'relativenumber'  'rnu'	    show relative line number in front of each line
Option: 'report'		    threshold for reporting nr. of lines changed
Option: 'revins'	  'ri'	    inserting characters will work backwards
Option: 'rightleft'	  'rl'	    window is right-to-left oriented
Option: 'rightleftcmd'	  'rlc'     commands for which editing works right-to-left
Option: 'ruler'		  'ru'	    show cursor line and column in the status line
Option: 'rulerformat'	  'ruf'     custom format for the ruler
Option: 'runtimepath'	  'rtp'     list of directories used for runtime files
Option: 'scroll'	  'scr'     lines to scroll with CTRL-U and CTRL-D
Option: 'scrollbind'	  'scb'     scroll in window as other windows scroll
Option: 'scrolljump'	  'sj'	    minimum number of lines to scroll
Option: 'scrolloff'	  'so'	    minimum nr. of lines above and below cursor
Option: 'scrollopt'	  'sbo'     how 'scrollbind' should behave
Option: 'sections'	  'sect'    nroff macros that separate sections
Option: 'secure'		    secure mode for reading .vimrc in current dir
Option: 'selection'	  'sel'     what type of selection to use
Option: 'selectmode'	  'slm'     when to use Select mode instead of Visual mode
Option: 'sessionoptions'  'ssop'    options for |:mksession|
Option: 'shada'		  'sd'	    use .shada file upon startup and exiting
Option: 'shell'		  'sh'	    name of shell to use for external commands
Option: 'shellcmdflag'	  'shcf'    flag to shell to execute one command
Option: 'shellpipe'	  'sp'	    string to put output of ":make" in error file
Option: 'shellquote'	  'shq'     quote character(s) for around shell command
Option: 'shellredir'	  'srr'     string to put output of filter in a temp file
Option: 'shellslash'	  'ssl'     use forward slash for shell file names
Option: 'shelltemp'	  'stmp'    whether to use a temp file for shell commands
Option: 'shellxescape'	  'sxe'     characters to escape when 'shellxquote' is (
Option: 'shellxquote'	  'sxq'     like 'shellquote', but include redirection
Option: 'shiftround'	  'sr'	    round indent to multiple of shiftwidth
Option: 'shiftwidth'	  'sw'	    number of spaces to use for (auto)indent step
Option: 'shortmess'	  'shm'     list of flags, reduce length of messages
Option: 'showbreak'	  'sbr'     string to use at the start of wrapped lines
Option: 'showcmd'	  'sc'	    show (partial) command somewhere
Option: 'showcmdloc'	  'sloc'    where to show (partial) command
Option: 'showfulltag'	  'sft'     show full tag pattern when completing tag
Option: 'showmatch'	  'sm'	    briefly jump to matching bracket if insert one
Option: 'showmode'	  'smd'     message on status line to show current mode
Option: 'showtabline'	  'stal'    tells when the tab pages line is displayed
Option: 'sidescroll'	  'ss'	    minimum number of columns to scroll horizontal
Option: 'sidescrolloff'   'siso'    min. nr. of columns to left and right of cursor
Option: 'signcolumn'	  'scl'	    when and how to display the sign column
Option: 'smartcase'	  'scs'     no ignore case when pattern has uppercase
Option: 'smartindent'	  'si'	    smart autoindenting for C programs
Option: 'smarttab'	  'sta'     use 'shiftwidth' when inserting <Tab>
Option: 'softtabstop'	  'sts'     number of spaces that <Tab> uses while editing
Option: 'spell'			    enable spell checking
Option: 'spellcapcheck'   'spc'     pattern to locate end of a sentence
Option: 'spellfile'	  'spf'     files where |zg| and |zw| store words
Option: 'spelllang'	  'spl'     language(s) to do spell checking for
Option: 'spelloptions'	  'spo'     options for spell checking
Option: 'spellsuggest'	  'sps'     method(s) used to suggest spelling corrections
Option: 'splitbelow'	  'sb'	    new window from split is below the current one
Option: 'splitkeep'	  'spk'     determines scroll behavior for split windows
Option: 'splitright'	  'spr'     new window is put right of the current one
Option: 'startofline'	  'sol'     commands move cursor to first non-blank in line
Option: 'statuscolumn'	  'stc'	    custom format for the status column
Option: 'statusline'	  'stl'     custom format for the status line
Option: 'suffixes'	  'su'	    suffixes that are ignored with multiple match
Option: 'suffixesadd'	  'sua'     suffixes added when searching for a file
Option: 'swapfile'	  'swf'     whether to use a swapfile for a buffer
Option: 'switchbuf'	  'swb'     sets behavior when switching to another buffer
Option: 'synmaxcol'	  'smc'     maximum column to find syntax items
Option: 'syntax'	  'syn'     syntax to be loaded for current buffer
Option: 'tabline'	  'tal'     custom format for the console tab pages line
Option: 'tabpagemax'	  'tpm'     maximum number of tab pages for |-p| and "tab all"
Option: 'tabstop'	  'ts'	    number of spaces that <Tab> in file uses
Option: 'tagbsearch'	  'tbs'     use binary searching in tags files
Option: 'tagcase'	  'tc'      how to handle case when searching in tags files
Option: 'tagfunc'	  'tfu'	    function to get list of tag matches
Option: 'taglength'	  'tl'	    number of significant characters for a tag
Option: 'tagrelative'	  'tr'	    file names in tag file are relative
Option: 'tags'		  'tag'     list of file names used by the tag command
Option: 'tagstack'	  'tgst'    push tags onto the tag stack
Option: 'term'			    name of the terminal
Option: 'termbidi'	  'tbidi'   terminal takes care of bi-directionality
Option: 'textwidth'	  'tw'	    maximum width of text that is being inserted
Option: 'thesaurus'	  'tsr'     list of thesaurus files for keyword completion
Option: 'thesaurusfunc'	  'tsrfu'   function to be used for thesaurus completion
Option: 'tildeop'	  'top'     tilde command "~" behaves like an operator
Option: 'timeout'	  'to'	    time out on mappings and key codes
Option: 'timeoutlen'	  'tm'	    time out time in milliseconds
Option: 'title'			    let Vim set the title of the window
Option: 'titlelen'		    percentage of 'columns' used for window title
Option: 'titleold'		    old title, restored when exiting
Option: 'titlestring'		    string to use for the Vim window title
Option: 'ttimeout'		    time out on mappings
Option: 'ttimeoutlen'	  'ttm'     time out time for key codes in milliseconds
Option: 'ttytype'	  'tty'     alias for 'term'
Option: 'undodir'	  'udir'    where to store undo files
Option: 'undofile'	  'udf'	    save undo information in a file
Option: 'undolevels'	  'ul'	    maximum number of changes that can be undone
Option: 'undoreload'	  'ur'	    max nr of lines to save for undo on a buffer reload
Option: 'updatecount'	  'uc'	    after this many characters flush swap file
Option: 'updatetime'	  'ut'	    after this many milliseconds flush swap file
Option: 'varsofttabstop'  'vsts'    a list of number of spaces when typing <Tab>
Option: 'vartabstop'	  'vts'	    a list of number of spaces for <Tab>s
Option: 'verbose'	  'vbs'     give informative messages
Option: 'verbosefile'	  'vfile'   file to write messages in
Option: 'viewdir'	  'vdir'    directory where to store files with :mkview
Option: 'viewoptions'	  'vop'     specifies what to save for :mkview
Option: 'virtualedit'	  've'	    when to use virtual editing
Option: 'visualbell'	  'vb'	    use visual bell instead of beeping
Option: 'warn'			    warn for shell command when buffer was changed
Option: 'whichwrap'	  'ww'	    allow specified keys to cross line boundaries
Option: 'wildchar'	  'wc'	    command-line character for wildcard expansion
Option: 'wildcharm'	  'wcm'     like 'wildchar' but also works when mapped
Option: 'wildignore'	  'wig'     files matching these patterns are not completed
Option: 'wildignorecase'  'wic'     ignore case when completing file names
Option: 'wildmenu'	  'wmnu'    use menu for command line completion
Option: 'wildmode'	  'wim'     mode for 'wildchar' command-line expansion
Option: 'wildoptions'	  'wop'     specifies how command line completion is done
Option: 'winaltkeys'	  'wak'     when the windows system handles ALT keys
Option: 'window'	  'wi'	    nr of lines to scroll for CTRL-F and CTRL-B
Option: 'winheight'	  'wh'	    minimum number of lines for the current window
Option: 'winhighlight'	  'winhl'   window-local highlighting
Option: 'winfixheight'	  'wfh'     keep window height when opening/closing windows
Option: 'winfixwidth'	  'wfw'     keep window width when opening/closing windows
Option: 'winminheight'	  'wmh'     minimum number of lines for any window
Option: 'winminwidth'	  'wmw'     minimal number of columns for any window
Option: 'winwidth'	  'wiw'     minimal number of columns for current window
Option: 'wrap'			    long lines wrap and continue on the next line
Option: 'wrapmargin'	  'wm'	    chars from the right where wrapping starts
Option: 'wrapscan'	  'ws'	    searches wrap around the end of the file
Option: 'write'			    writing to a file is allowed
Option: 'writeany'	  'wa'	    write to file with no need for "!" override
Option: 'writebackup'	  'wb'	    make a backup before overwriting a file
Option: 'writedelay'	  'wd'	    delay this many msec for each char (for debug)
|u|       N  u		undo last N changes
|CTRL-R|  N  CTRL-R	redo last N undone changes
|U|          U		restore last changed line
|:!|		:!{command}	execute {command} with a shell
|K|		   K		lookup keyword under the cursor with 'keywordprg' program (default: "man")
|:cc|		:cc [nr]	display error [nr] (default is the same again)
|:cnext|	:cn		display the next error
|:cprevious|	:cp		display the previous error
|:clist|	:cl		list all errors
|:cfile|	:cf		read errors from the file 'errorfile'
|:cgetbuffer|	:cgetb		like :cbuffer but don't jump to the first error
|:cgetfile|	:cg		like :cfile but don't jump to the first error
|:cgetexpr|	:cgete		like :cexpr but don't jump to the first error
|:caddfile|	:caddf		add errors from the error file to the current quickfix list
|:caddexpr|	:cad		add errors from an expression to the current quickfix list
|:cbuffer|	:cb		read errors from text in a buffer
|:cexpr|	:cex		read errors from an expression
|:cquit|	:cq		quit without writing and return error code (to the compiler)
|:make|		:make [args]	start make, read errors, and jump to first error
|:grep|		:gr[ep] [args]	execute 'grepprg' to find matches and jump to the first one
|CTRL-L|	   CTRL-L	clear and redraw the screen
|CTRL-G|	   CTRL-G	show current file name (with path) and cursor position
|ga|		   ga		show ascii value of character under cursor in decimal, hex, and octal
|g8|		   g8		for utf-8 encoding: show byte sequence for character under cursor in hex
|g_CTRL-G|	   g CTRL-G	show cursor column, line, and character position
|CTRL-C|	   CTRL-C	during searches: Interrupt the search
|<Del>|		   <Del>	while entering a count: delete last character
|:version|	:ve[rsion]	show version information
|:normal|	:norm[al][!] {commands} execute Normal mode commands
|gQ|		   gQ		switch to "Ex" mode
|:redir|	:redir >{file}		redirect messages to {file}
|:silent|	:silent[!] {command}	execute {command} silently
|:confirm|	:confirm {command}	quit, write, etc., asking about unsaved changes or read-only files
|:browse|	:browse {command}	open/read/write file, using a file selection dialog
|c_<Esc>|	<Esc>		   abandon command-line (if 'wildchar' is <Esc>, type it twice)
|c_CTRL-V|	CTRL-V {char}	   insert {char} literally
|c_CTRL-V|	CTRL-V {number}    enter decimal value of character (up to three digits)
|c_CTRL-K|	CTRL-K {char1} {char2} enter digraph (See |Q_di|)
|c_CTRL-R|	CTRL-R {register}  insert the contents of a register
|c_<Left>|	<Left>/<Right>	   cursor left/right
|c_<S-Left>|	<S-Left>/<S-Right> cursor one word left/right
|c_CTRL-B|	CTRL-B/CTRL-E	   cursor to beginning/end of command-line
|c_<BS>|	<BS>		   delete the character in front of the cursor
|c_<Del>|	<Del>		   delete the character under the cursor
|c_CTRL-W|	CTRL-W		   delete the word in front of the cursor
|c_CTRL-U|	CTRL-U		   remove all characters
|c_<Up>|	<Up>/<Down>	   recall older/newer command-line that starts with current command
|c_<S-Up>|	<S-Up>/<S-Down>	   recall older/newer command-line from history
|c_CTRL-G|	CTRL-G		   next match when 'incsearch' is active
|c_CTRL-T|	CTRL-T		   previous match when 'incsearch' is active
|:history|	:his[tory]	   show older command-lines
|c_wildchar|	'wildchar'  (default: <Tab>) do completion on the pattern in front of the cursor; if there are multiple matches, beep and show the first one; further 'wildchar' will show the next ones
|c_CTRL-D|	CTRL-D		list all names that match the pattern in front of the cursor
|c_CTRL-A|	CTRL-A		insert all names that match pattern in front of cursor
|c_CTRL-L|	CTRL-L		insert longest common part of names that match pattern
|c_CTRL-N|	CTRL-N		after 'wildchar' with multiple matches: go to next match
|c_CTRL-P|	CTRL-P		after 'wildchar' with multiple matches: go to previous match
|:range|	,		separates two line numbers
|:range|	;		separates two line numbers, set cursor to the first line number before interpreting the second one
|:range|	{number}	an absolute line number
|:range|	.		the current line
|:range|	$		the last line in the file
|:range|	%		equal to 1,$ (the entire file)
|:range|	*		equal to '<,'> (visual area)
|:range|	't		position of mark t
|:range|	/{pattern}[/]	the next line where {pattern} matches
|:range|	?{pattern}[?]	the previous line where {pattern} matches
|:range|	+[num]		add [num] to the preceding line number (default: 1)
|:range|	-[num]		subtract [num] from the preceding line number (default: 1)
|:bar|      |		separates two commands (not for ":global" and ":!")
|:quote|    "		begins comment
|:_%|       %		current file name (only where a file name is expected)
|:_#|       #[num]	alternate file name [num] (only where a file name is expected). The next seven are typed literally; these are not special keys!
|:<abuf>|   <abuf>	buffer number, for use in an autocommand (only where a file name is expected)
|:<afile>|  <afile>	file name, for use in an autocommand (only where a file name is expected)
|:<amatch>| <amatch>	what matched with the pattern, for use in an autocommand (only where a file name is expected)
|:<cword>|  <cword>	word under the cursor (only where a file name is expected)
|:<cWORD>|  <cWORD>	WORD under the cursor (only where a file name is expected) (see |WORD|)
|:<cfile>|  <cfile>	file name under the cursor (only where a file name is expected)
|:<sfile>|  <sfile>	file name of a ":source"d file, within that file (only where a file name is expected)
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::p|	    :p		full path
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::h|	    :h		head (file name removed)
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::t|	    :t		tail (file name only)
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::r|	    :r		root (extension removed)
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::e|	    :e		extension
Command line, after "%", "#", "<cfile>", "<sfile>" or "<afile>"		|::s|	    :s/{pat}/{repl}/	substitute {pat} with {repl}
vim command option: |-file|	   vim [options] {file} ..	start editing one or more files
vim command option: |--|	   vim [options] -		read file from stdin
vim command option: |-tag|	   vim [options] -t {tag}	edit the file associated with {tag}
vim command option: |-qf|	   vim [options] -q [fname]	start editing in QuickFix mode, display the first error
vim command option: |-+|	+[num]		    put the cursor at line [num] (default: last line)
vim command option: |-+c|	+{command}	    execute {command} after loading the file
vim command option: |-+/|	+/{pat} {file} ..   put the cursor at the first occurrence of {pat}
vim command option: |-e|	-e		    Ex mode, start vim in Ex mode
vim command option: |-R|	-R		    Read-only mode, implies -n
vim command option: |-m|	-m		    modifications not allowed (resets 'write' option)
vim command option: |-d|	-d		    |diff-mode|
vim command option: |-b|	-b		    binary mode
vim command option: |-l|	-l		    lisp mode
vim command option: |-A|	-A		    Arabic mode ('arabic' is set)
vim command option: |-H|	-H		    Hebrew mode ('hkmap' and 'rightleft' are set)
vim command option: |-V|	-V		    Verbose, give informative messages
vim command option: |-r|	-r		    give list of swap files
vim command option: |-r|	-r {file} ..	    recover aborted edit session
vim command option: |-n|	-n		    do not create a swap file
vim command option: |-o|	-o [num]	    open [num] windows (default: one for each file)
vim command option: |-s|	-s {scriptin}	    first read commands from the file {scriptin}
vim command option: |-w|	-w {scriptout}	    write typed chars to file {scriptout} (append)
vim command option: |-W|	-W {scriptout}	    write typed chars to file {scriptout} (overwrite)
vim command option: |-u|	-u {vimrc}	    read inits from {vimrc} instead of other inits
vim command option: |-i|	-i {shada}	    read info from {shada} instead of other files
vim command option: |---|	--		    end of options, other arguments are file names
vim command option: |--help|    --help	    show list of arguments and exit
vim command option: |--version| --version	    show version info and exit
vim command option: |--|	-		    read file from stdin
|:edit_f|  :e[dit][!] {file}	edit {file}
|:edit|    :e[dit][!]		reload the current file
|:enew|    :ene[w][!]		edit a new, unnamed buffer
|:find|    :fin[d][!] {file}	find {file} in 'path' and edit it
|CTRL-^|   N  CTRL-^		edit alternate file N (equivalent to ":e #N")
|gf|          gf  or ]f		edit the file whose name is under the cursor
|:pwd|     :pwd			print the current directory name
|:cd|      :cd [path]		change the current directory to [path]
|:cd-|     :cd -		back to previous current directory
|:file|    :f[ile]		print the current file name and the cursor position
|:file|    :f[ile] {name}	set the current file name to {name}
|:files|   :files		show alternate file names
|:args|	   :ar[gs]		print the argument list, with the current file in "[]"
|:all|	   :all  or :sall	open a window for every file in the arg list
|:wn|	   :wn[ext][!]		write file and edit next file
|:wn|	   :wn[ext][!] {file}	write to {file} and edit next file, unless {file} exists; With !, overwrite existing file
|:wN|	   :wN[ext][!] [file]	write file and edit previous file
|:argument|  :argu[ment] N	  :sar[gument] N	edit file N
|:next|      :n[ext]		  :sn[ext]		edit next file
|:next_f|    :n[ext] {arglist}	  :sn[ext] {arglist}	define new arg list and edit first file
|:Next|      :N[ext]		  :sN[ext]		edit previous file
|:first|     :fir[st]		  :sfir[st]		edit first file
|:last|      :la[st]		  :sla[st]		edit last file
|:w|	  :[range]w[rite][!]		write to the current file
|:w_f|	  :[range]w[rite] {file}	write to {file}, unless it already exists
|:w_f|	  :[range]w[rite]! {file}	write to {file}.  Overwrite an existing file
|:w_a|	  :[range]w[rite][!] >>		append to the current file
|:w_a|	  :[range]w[rite][!] >> {file}	append to {file}
|:w_c|	  :[range]w[rite] !{cmd}	execute {cmd} with [range] lines as standard input
|:up|	  :[range]up[date][!]		write to current file if modified
|:wall|	  :wa[ll][!]			write all changed buffers
|:q|	  :q[uit]		quit current buffer, unless changes have been made; Exit Vim when there are no other non-help buffers
|:q|	  :q[uit]!		quit current buffer always, discard any changes.  Exit Vim when there are no other non-help buffers
|:qa|	  :qa[ll]		exit Vim, unless changes have been made
|:qa|	  :qa[ll]!		exit Vim always, discard any changes
|:cq|	  :cq			quit without writing and return error code
|:wq|	  :wq[!]		write the current file and exit
|:wq|	  :wq[!] {file}		write to {file} and exit
|:xit|	  :x[it][!] [file]	like ":wq" but write only when changes have been made
|ZZ|	     ZZ			same as ":x"
|ZQ|	     ZQ			same as ":q!"
|:xall|	  :xa[ll][!]  or :wqall[!] write all changed buffers and exit
|:stop|	  :st[op][!]		suspend Vim or start new shell; if 'aw' option is set and [!] not given write the buffer
|CTRL-Z|     CTRL-Z		same as ":stop"
|:rshada|	:rsh[ada] [file]	read info from ShaDa file [file]
|:rshada|	:rsh[ada]! [file]	read info from ShaDa file, overwrite existing info
|:wshada|	:wsh[ada] [file]	add info to ShaDa file [file]
|:wshada|	:wsh[ada]! [file]	write info to ShaDa file [file]
|:autocmd|	:au			  list all autocommands
|:autocmd|	:au {event}		  list all autocommands for {event}
|:autocmd|	:au {event} {pat}	  list all autocommands for {event} with {pat}
|:autocmd|	:au {event} {pat} {cmd}	  enter new autocommands for {event} with {pat}
|:autocmd|	:au!			  remove all autocommands
|:autocmd|	:au! {event}		  remove all autocommands for {event}
|:autocmd|	:au! * {pat}		  remove all autocommands for {pat}
|:autocmd|	:au! {event} {pat}	  remove all autocommands for {event} with {pat}
|:autocmd|	:au! {event} {pat} {cmd}  remove all autocommands for {event} with {pat} and enter new one
|CTRL-W_s|	CTRL-W s  or  :split	split window into two parts
|:split_f|	:split {file}		split window and edit {file} in one of them
|:vsplit|	:vsplit {file}		same, but split vertically
|:vertical|	:vertical {cmd}		make {cmd} split vertically
|:sfind|	:sf[ind] {file}		split window, find {file} in 'path' and edit it
|:terminal|	:terminal {cmd}		open a terminal window
|CTRL-W_]|	CTRL-W ]		split window and jump to tag under cursor
|CTRL-W_f|	CTRL-W f		split window and edit file name under the cursor
|CTRL-W_^|	CTRL-W ^		split window and edit alternate file
|CTRL-W_n|	CTRL-W n  or  :new	create new empty window
|CTRL-W_q|	CTRL-W q  or  :q[uit]	quit editing and close window
|CTRL-W_c|	CTRL-W c  or  :clo[se]	make buffer hidden and close window
|CTRL-W_o|	CTRL-W o  or  :on[ly]	make current window only one on the screen
|CTRL-W_j|	CTRL-W j		move cursor to window below
|CTRL-W_k|	CTRL-W k		move cursor to window above
|CTRL-W_CTRL-W|	CTRL-W CTRL-W		move cursor to window below (wrap)
|CTRL-W_W|	CTRL-W W		move cursor to window above (wrap)
|CTRL-W_t|	CTRL-W t		move cursor to top window
|CTRL-W_b|	CTRL-W b		move cursor to bottom window
|CTRL-W_p|	CTRL-W p		move cursor to previous active window
|CTRL-W_r|	CTRL-W r		rotate windows downwards
|CTRL-W_R|	CTRL-W R		rotate windows upwards
|CTRL-W_x|	CTRL-W x		exchange current window with next one
|CTRL-W_=|	CTRL-W =		make all windows equal height & width
|CTRL-W_-|	CTRL-W -		decrease current window height
|CTRL-W_+|	CTRL-W +		increase current window height
|CTRL-W__|	CTRL-W _		set current window height (default: very high)
|CTRL-W_<|	CTRL-W <		decrease current window width
|CTRL-W_>|	CTRL-W >		increase current window width
|CTRL-W_bar|	CTRL-W |		set current window width (default: widest possible)
|:buffers|	:buffers  or  :files	list all known buffer and file names
|:ball|		:ball	  or  :sball	edit all args/buffers
|:unhide|	:unhide   or  :sunhide	edit all loaded buffers
|:badd|		:badd {fname}		add file name {fname} to the list
|:bunload|	:bunload[!] [N]		unload buffer [N] from memory
|:bdelete|	:bdelete[!] [N]		unload buffer [N] and delete it from the buffer list
|:buffer|	:[N]buffer [N]     :[N]sbuffer [N]     to arg/buf N
|:bnext|	:[N]bnext [N]      :[N]sbnext [N]      to Nth next arg/buf
|:bNext|	:[N]bNext [N]      :[N]sbNext [N]      to Nth previous arg/buf
|:bprevious|	:[N]bprevious [N]  :[N]sbprevious [N]  to Nth previous arg/buf
|:bfirst|	:bfirst	           :sbfirst            to first arg/buf
|:blast|	:blast	           :sblast             to last arg/buf
|:bmodified|	:[N]bmod [N]       :[N]sbmod [N]       to Nth modified buf
|:syn-on|	:syntax on		start using syntax highlighting
|:syn-off|	:syntax off		stop using syntax highlighting
|:syn-keyword|	:syntax keyword {group-name} {keyword} .. add a syntax keyword item
|:syn-match|	:syntax match {group-name} {pattern} ... add syntax match item
|:syn-region|	:syntax region {group-name} {pattern} ... add syntax region item
|:syn-sync|	:syntax sync [ccomment | lines {N} | ...] tell syntax how to sync
|:syntax|	:syntax [list]		list current syntax items
|:syn-clear|	:syntax clear		clear all syntax info
|:highlight|	:highlight clear	clear all highlight info
|:highlight|	:highlight {group-name} {key}={arg} .. set highlighting for {group-name}
|:filetype|	:filetype on		switch on file type detection, without syntax highlighting
|:filetype|	:filetype plugin indent on switch on file type detection, with automatic indenting and settings
|:menu|		:menu			list all menus
|:menu|		:menu {mpath}		list menus starting with {mpath}
|:menu|		:menu {mpath} {rhs}	add menu {mpath}, giving {rhs}
|:menu|		:menu {pri} {mpath} {rhs} add menu {mpath}, giving {rhs} with priorities {pri}
|:menu|		:menu ToolBar.{name} {rhs} add toolbar item, giving {rhs}
|:tmenu|	:tmenu {mpath} {text}	add tooltip to menu {mpath}
|:unmenu|	:unmenu {mpath}		remove menu {mpath}
|'foldmethod'|	set foldmethod=manual	manual folding, set foldmethod=indent	folding by indent, set foldmethod=expr	folding by 'foldexpr', set foldmethod=syntax	folding by syntax regions, set foldmethod=marker	folding by 'foldmarker'
|zf|		zf{motion}		operator: Define a fold manually
|:fold|		:{range}fold		define a fold for {range} lines
|zd|		zd			delete one fold under the cursor
|zD|		zD			delete all folds under the cursor
|zo|		zo			open one fold under the cursor
|zO|		zO			open all folds under the cursor
|zc|		zc			close one fold under the cursor
|zC|		zC			close all folds under the cursor
|zm|		zm			fold more: decrease 'foldlevel'
|zM|		zM			close all folds: make 'foldlevel' zero
|zr|		zr			reduce folding: increase 'foldlevel'
|zR|		zR			open all folds: make 'foldlevel' max.
|zn|		zn			fold none: reset 'foldenable'
|zN|		zN			fold normal set 'foldenable'
|zi|		zi			invert 'foldenable'"""

index = [2176, 1678, 296, 95, 280, 1370, 905, 1570, 1669, 2083, 376, 1123, 1708, 1800, 1483, 1522, 1511, 1289, 1437, 260, 187, 1010, 2088, 776, 949, 241, 1367, 362, 313, 966, 758, 791, 382, 224, 2081, 1089, 2129, 1665, 1941, 742, 1357, 292, 664, 869, 1359, 1332, 1714, 2031, 1077, 716, 1006, 347, 1780, 1161, 1559, 205, 831, 1086, 911, 2107, 828, 441, 1368, 1081, 219, 1996, 821, 1896, 1209, 255, 1304, 2022, 1506, 1930, 1263, 1742, 1429, 1366, 314, 148, 1288, 2173, 462, 173, 368, 1096, 692, 670, 514, 950, 1297, 1700, 1694, 612, 1451, 736, 765, 430, 1809, 987, 1764, 1069, 601, 695, 1977, 2098, 1036, 59, 123, 1968, 243, 10, 767, 1569, 1281, 1274, 1635, 1865, 974, 690, 170, 1580, 917, 734, 425, 1243, 1910, 1345, 654, 1850, 492, 251, 225, 1005, 726, 624, 1335, 1145, 178, 1410, 1210, 232, 140, 122, 1037, 1218, 1767, 357, 1237, 1906, 1014, 889, 460, 1932, 1266, 1109, 1182, 48, 17, 986, 2105, 674, 583, 1820, 1803, 1892, 331, 334, 2032, 1339, 413, 992, 325, 1227, 62, 1663, 1684, 968, 1376, 545, 254, 1723, 1972, 593, 28, 1457, 1897, 172, 597, 1541, 777, 1848, 272, 14, 961, 423, 1083, 1021, 67, 261, 2168, 1125, 2165, 1662, 1143, 437, 1948, 2142, 2172, 2094, 1987, 1380, 1259, 342, 2154, 365, 706, 751, 626, 353, 402, 480, 502, 580, 1331, 1087, 440, 1054, 1261, 1652, 91, 2096, 33, 372, 1196, 209, 1168, 114, 1476, 297, 277, 1157, 2068, 295, 1189, 2155, 436, 256, 676, 1296, 471, 1469, 1702, 301, 687, 1971, 1233, 577, 1759, 1124, 218, 1349, 2082, 948, 1862, 2009, 1839, 101, 1249, 2127, 1023, 570, 1818, 1851, 273, 2125, 1072, 5, 16, 322, 500, 1056, 1826, 1600, 2047, 2093, 1310, 1148, 1628, 113, 70, 686, 2174, 1484, 1216, 1240, 1030, 1133, 1738, 901, 2045, 473, 1160, 2012, 1873, 528, 1785, 1085, 4, 2179, 1991, 1614, 2122, 472, 1647, 1252, 1450, 2043, 1230, 611, 2144, 1888, 1833, 2057, 2019, 1302, 1589, 2171, 801, 1372, 475, 237, 1595, 1111, 1638, 0, 1646, 1329, 1794, 501, 390, 1810, 360, 2151, 883, 1058, 1727, 1715, 779, 2013, 1127, 1668, 519, 2102, 995, 324, 700, 1557, 2033, 691, 1208, 489, 1611, 288, 1598, 64, 1813, 231, 112, 892, 672, 443, 1308, 1397, 2016, 1951, 1682, 573, 1963, 939, 412, 411, 2078, 1527, 98, 2111, 214, 327, 238, 566, 1924, 1591, 1479, 1122, 391, 1520, 639, 1835, 1866, 1553, 718, 698, 27, 782, 1354, 894, 1283, 1353, 1957, 752, 1200, 1656, 2139, 1967, 2124, 513, 669, 21, 1875, 688, 958, 57, 880, 1825, 2059, 1432, 850, 478, 2072, 433, 2146, 1619, 1438, 1993, 389, 1736, 1613, 784, 919, 499, 22, 130, 960, 814, 1285, 836, 1251, 957, 1760, 1720, 1220, 1256, 1132, 1961, 1441, 1198, 1707, 1253, 374, 1194, 2167, 1686, 652, 346, 998, 401, 257, 1801, 1337, 635, 1761, 796, 711, 790, 1999, 908, 1724, 152, 817, 202, 1837, 1184, 1945, 1170, 1854, 1136, 1849, 1806, 1340, 701, 1838, 903, 689, 1828, 884, 983, 996, 531, 1494, 797, 2106, 451, 1545, 1728, 2010, 762, 2170, 1205, 1231, 704, 1781, 69, 1065, 813, 1867, 587, 2014, 1293, 1984, 1855, 30, 448, 399, 490, 615, 944, 468, 100, 1970, 963, 838, 568, 429, 2006, 973, 216, 1126, 1103, 526, 1644, 1020, 2099, 509, 794, 1146, 866, 1301, 1532, 164, 378, 2025, 1797, 772, 826, 1435, 773, 972, 520, 2054, 1166, 970, 1974, 1642, 1306, 300, 841, 1341, 1615, 1776, 55, 1361, 1755, 832, 1071, 1606, 397, 1622, 840, 1763, 321, 663, 1186, 424, 2121, 1095, 141, 121, 2113, 1102, 12, 1199, 1554, 1385, 1952, 483, 1573, 798, 25, 305, 1326, 761, 1926, 1107, 1112, 1929, 709, 268, 1012, 2118, 1683, 2143, 667, 128, 1805, 117, 793, 1076, 2064, 955, 1236, 326, 1393, 849, 1513, 1247, 2175, 1745, 1179, 1412, 264, 66, 1459, 1299, 1792, 306, 1330, 421, 407, 1583, 1300, 1409, 685, 1889, 1118, 1581, 491, 1582, 534, 298, 143, 1816, 44, 392, 431, 75, 1817, 479, 1423, 1444, 1966, 940, 757, 2058, 1343, 1710, 1338, 228, 1434, 1754, 1197, 754, 1238, 1344, 215, 161, 439, 1979, 88, 1242, 380, 386, 487, 1594, 1853, 307, 830, 65, 912, 1391, 766, 340, 1883, 1082, 2008, 145, 1499, 1958, 1092, 1857, 1703, 1725, 1460, 879, 328, 166, 1909, 1456, 544, 466, 980, 1320, 873, 1319, 1904, 1395, 1138, 1420, 933, 1149, 302, 638, 989, 636, 1603, 1734, 661, 1358, 60, 1880, 116, 1901, 457, 746, 40, 1180, 1064, 537, 1191, 1232, 1413, 124, 642, 265, 1863, 530, 1399, 753, 341, 19, 2056, 1689, 1519, 1348, 953, 1490, 1864, 1586, 43, 2177, 1011, 952, 1165, 13, 931, 1542, 941, 1016, 681, 1827, 2149, 848, 1921, 1215, 1908, 1894, 1555, 1852, 1307, 1922, 984, 1566, 1489, 527, 149, 497, 449, 769, 1627, 1162, 678, 1025, 1898, 2003, 2126, 1286, 857, 665, 1154, 435, 293, 267, 1534, 184, 792, 1537, 85, 512, 1698, 1944, 1169, 244, 336, 177, 2071, 1110, 2077, 23, 120, 1436, 183, 523, 1117, 1425, 1428, 991, 1811, 658, 469, 350, 827, 2116, 1185, 810, 1356, 1657, 878, 1659, 703, 249, 495, 620, 111, 510, 853, 876, 246, 2015, 1918, 52, 329, 1134, 1861, 1019, 1610, 1031, 46, 1467, 409, 92, 978, 1104, 180, 1067, 1094, 1752, 2036, 2115, 1481, 677, 108, 1381, 181, 749, 1660, 1798, 843, 464, 1990, 271, 1690, 2069, 729, 1156, 1486, 1869, 1782, 285, 253, 1617, 351, 895, 1766, 1618, 997, 1488, 1044, 1244, 713, 131, 1292, 18, 1055, 1783, 320, 1969, 1369, 1704, 442, 2041, 2166, 1661, 990, 242, 1729, 1804, 319, 598, 1981, 1049, 1038, 845, 118, 308, 1701, 979, 632, 887, 1942, 398, 1762, 2039, 2029, 1221, 551, 1407, 1640, 877, 590, 165, 1732, 1246, 1843, 1571, 1623, 1379, 1426, 1982, 671, 942, 914, 1900, 488, 956, 943, 507, 1041, 126, 133, 964, 160, 49, 1917, 702, 1091, 921, 1068, 803, 1985, 227, 1919, 1773, 852, 1360, 835, 182, 1681, 1500, 747, 649, 1911, 1445, 981, 1751, 167, 872, 1113, 1105, 284, 1538, 2044, 1001, 855, 947, 1913, 245, 552, 20, 1207, 1564, 1831, 1212, 1009, 373, 1027, 1771, 496, 899, 1222, 2128, 1834, 345, 594, 93, 885, 712, 1311, 1362, 760, 461, 2158, 959, 1229, 1454, 2080, 263, 303, 1473, 1114, 1868, 1250, 1495, 1743, 825, 1468, 1206, 79, 1219, 517, 1287, 675, 1933, 47, 134, 786, 1793, 1175, 1097, 1139, 1750, 1464, 53, 444, 748, 1770, 1802, 1417, 1608, 274, 1017, 1588, 1629, 2109, 1605, 723, 1268, 549, 2065, 1276, 1989, 975, 1100, 1098, 763, 416, 1830, 1140, 31, 668, 259, 1572, 516, 2042, 745, 1024, 438, 1539, 1277, 132, 1688, 656, 250, 356, 1886, 1352, 1392, 1448, 735, 2163, 1959, 470, 417, 54, 542, 1452, 854, 1290, 621, 616, 51, 1870, 976, 1147, 2034, 1634, 1937, 151, 1840, 1492, 1753, 1549, 1836, 811, 175, 1535, 1510, 1502, 222, 1315, 600, 2001, 1406, 851, 477, 1709, 426, 1371, 1975, 787, 1860, 2052, 1994, 1325, 802, 1847, 1203, 822, 388, 1272, 1735, 1422, 275, 1333, 6, 73, 1503, 1893, 646, 865, 211, 2040, 2066, 179, 891, 142, 650, 456, 1524, 2147, 1558, 446, 385, 1318, 1383, 1748, 1474, 1528, 1491, 26, 1470, 1949, 515, 310, 1059, 1905, 1405, 343, 287, 1322, 927, 1128, 896, 1003, 907, 7, 557, 156, 581, 2090, 485, 1552, 1482, 428, 934, 1347, 1884, 666, 1378, 910, 2097, 2120, 1841, 1364, 104, 1680, 550, 1585, 799, 1697, 1043, 1936, 1824, 1355, 2084, 684, 364, 135, 506, 1144, 34, 846, 1181, 1846, 240, 1183, 2002, 775, 1328, 1382, 780, 768, 993, 107, 724, 463, 348, 1556, 2028, 2101, 574, 1130, 660, 1497, 804, 833, 1912, 427, 1008, 1202, 721, 139, 2148, 1346, 1440, 1692, 1658, 1309, 1278, 842, 8, 1075, 366, 1235, 1314, 1821, 584, 1509, 1267, 414, 722, 571, 1973, 605, 1812, 1282, 77, 1174, 965, 2136, 824, 1523, 1294, 369, 733, 247, 2134, 657, 289, 119, 45, 2160, 1737, 1461, 2026, 2089, 1398, 58, 2000, 2140, 1141, 210, 1026, 191, 1590, 1142, 708, 1885, 204, 694, 367, 221, 383, 35, 1084, 1159, 190, 1453, 774, 834, 1151, 1050, 482, 1153, 511, 339, 1786, 1960, 1576, 967, 918, 1667, 1655, 1201, 562, 592, 248, 2050, 1525, 2108, 1129, 1260, 1485, 682, 1526, 1551, 318, 1774, 80, 1859, 819, 90, 913, 162, 2156, 1718, 897, 102, 1264, 1119, 2005, 999, 1964, 2095, 1907, 868, 741, 1876, 539, 627, 1463, 332, 335, 193, 1916, 1093, 1375, 36, 1599, 1350, 163, 1928, 648, 410, 2164, 1693, 2112, 1612, 1962, 74, 898, 1992, 29, 928, 837, 1060, 540, 110, 543, 1756, 84, 881, 1262, 315, 1028, 1073, 607, 192, 1390, 533, 738, 1633, 875, 737, 1099, 1121, 358, 1795, 1943, 807, 125, 1164, 1540, 2178, 565, 863, 1965, 870, 994, 1228, 629, 1632, 147, 1631, 610, 2092, 1533, 24, 311, 1954, 800, 596, 1666, 1978, 715, 1823, 564, 2091, 2159, 2049, 1630, 82, 864, 1172, 1193, 937, 129, 861, 1269, 1108, 618, 1517, 2153, 1275, 1000, 720, 553, 1940, 1858, 575, 1214, 1650, 1458, 1401, 338, 977, 1377, 1621, 1115, 839, 696, 42, 266, 355, 1433, 644, 619, 1579, 1664, 1927, 806, 818, 1, 381, 9, 203, 2180, 465, 631, 1616, 1061, 138, 32, 1271, 1562, 1648, 1675, 1654, 567, 159, 1303, 743, 2086, 555, 2131, 1515, 1574, 859, 279, 634, 1327, 1013, 2162, 546, 1386, 1673, 588, 474, 1620, 1192, 406, 1778, 969, 418, 710, 1384, 1455, 920, 1475, 1879, 484, 697, 613, 604, 1101, 197, 602, 653, 693, 572, 1923, 847, 1365, 1466, 2074, 1178, 1255, 419, 450, 2060, 1057, 1487, 1498, 1947, 2145, 1424, 99, 1670, 717, 727, 1915, 2133, 608, 2048, 1674, 815, 504, 1592, 452, 890, 641, 1045, 1596, 1758, 809, 524, 200, 829, 1514, 2076, 2161, 844, 795, 2100, 41, 1035, 662, 2085, 1653, 2053, 1416, 1733, 1871, 276, 230, 673, 1881, 1597, 1721, 377, 1955, 1478, 1034, 714, 1447, 189, 61, 1531, 1317, 208, 1471, 1176, 1280, 1504, 384, 2157, 705, 731, 212, 929, 1004, 408, 522, 808, 1565, 1550, 781, 1530, 1312, 199, 938, 871, 1270, 683, 582, 1106, 788, 1173, 1396, 617, 195, 150, 1636, 1899, 1295, 486, 750, 647, 563, 1254, 2141, 1567, 2075, 1887, 744, 576, 1529, 1291, 1643, 2062, 1749, 558, 445, 363, 985, 349, 1507, 730, 2017, 1225, 2020, 1671, 732, 538, 1568, 11, 559, 659, 1258, 645, 770, 1032, 569, 1171, 105, 234, 1639, 1408, 1512, 447, 1224, 171, 935, 361, 1988, 1938, 103, 971, 258, 505, 2137, 1042, 1706, 459, 1239, 1578, 740, 609, 415, 503, 127, 1705, 137, 707, 725, 1415, 317, 988, 3, 1696, 2007, 56, 823, 68, 1891, 2135, 1547, 1204, 375, 72, 606, 1609, 76, 764, 1190, 154, 1022, 1167, 945, 290, 771, 1877, 89, 354, 2079, 185, 1496, 2063, 1187, 874, 625, 281, 2061, 207, 223, 2132, 330, 1048, 15, 755, 1414, 1593, 400, 1323, 614, 1135, 405, 2152, 1051, 1716, 1878, 1446, 403, 168, 252, 1090, 1388, 1548, 2087, 1394, 1324, 1211, 1712, 1914, 1713, 756, 2055, 1508, 1995, 904, 1351, 1895, 270, 1584, 1439, 1997, 371, 87, 1040, 1245, 1575, 1726, 536, 1387, 1815, 194, 1685, 1177, 1316, 2024, 434, 63, 579, 1079, 622, 269, 1874, 359, 1002, 1418, 1273, 1624, 476, 1053, 1472, 1279, 1195, 640, 196, 1334, 925, 1158, 2150, 1687, 146, 1404, 115, 1234, 2038, 395, 1626, 1442, 1257, 541, 153, 422, 860, 1842, 94, 1039, 393, 888, 1313, 1649, 1163, 982, 1560, 498, 858, 198, 226, 333, 176, 946, 886, 312, 1505, 1400, 1789, 1986, 699, 1155, 1796, 916, 719, 867, 651, 1462, 728, 924, 1902, 1536, 1080, 1788, 1131, 560, 521, 1430, 2067, 1033, 2, 1676, 923, 585, 2114, 278, 1637, 1931, 109, 174, 1832, 458, 454, 1493, 71, 1029, 547, 455, 1248, 453, 1882, 906, 1829, 1516, 1677, 1342, 900, 2117, 1088, 1814, 1305, 930, 1722, 144, 561, 623, 1787, 1284, 1217, 1920, 816, 86, 589, 1052, 1015, 1047, 1078, 309, 1953, 1421, 206, 1890, 1449, 97, 283, 1336, 2070, 1744, 1563, 2138, 396, 1711, 1188, 1625, 83, 96, 525, 936, 554, 1672, 2103, 38, 1790, 299, 1731, 1062, 785, 812, 1845, 1063, 1363, 213, 1265, 1717, 932, 882, 1116, 1746, 739, 282, 106, 78, 220, 1604, 1443, 136, 294, 1757, 235, 158, 1389, 1772, 679, 394, 1768, 1298, 2027, 1934, 1741, 1402, 508, 951, 186, 2011, 1546, 1775, 1543, 2037, 603, 2051, 1939, 856, 655, 1946, 820, 1427, 962, 1213, 39, 529, 1872, 1769, 239, 909, 915, 37, 432, 532, 1226, 2130, 1120, 1411, 1544, 1223, 1976, 188, 286, 2035, 595, 337, 1699, 201, 493, 862, 637, 805, 316, 1903, 680, 1321, 2169, 633, 789, 1777, 922, 1691, 556, 586, 217, 1602, 1730, 2123, 578, 1779, 1066, 1651, 1241, 233, 352, 1956, 404, 1819, 157, 1431, 1521, 50, 518, 902, 1074, 1925, 1007, 2018, 1374, 387, 1791, 1419, 954, 1740, 1983, 2104, 379, 81, 1501, 2023, 1641, 2021, 1046, 2110, 1373, 1844, 1607, 1998, 1018, 1645, 1950, 262, 1152, 1784, 1150, 1480, 1807, 628, 893, 1679, 1518, 304, 643, 1719, 344, 420, 1137, 1601, 1739, 1577, 1822, 1465, 778, 759, 1808, 2046, 599, 481, 155, 535, 1477, 1856, 370, 926, 2073, 494, 1980, 2030, 229, 1587, 467, 1695, 630, 2119, 169, 1561, 1799, 236, 548, 323, 1403, 1070, 2004, 591, 1935, 291, 1747, 783, 1765]
import time
data = ROM.split('\n')
N = len(data)
print(' ', data[index[int(int(time.time())/(6*3600))%N]])
