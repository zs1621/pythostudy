##理解parse_command_line


def parse_command_line(self, args=None, final=True):
	"""
	解析所有的配置.注意'args[0]'是被忽略的因为它指的是运行的文件。"""

	if args is None:
		args = sys.argv
	remaining = []

	for i in range(1, len(args)):
		if not args[i].startswith("-"):
			remaining = args[i]
			break
		if args[i] == "--":
			remaining = args[i + 1:]
			break
		arg = args[i].lstrip("-") #lstrip 除去左边的字符
		name, equals, value = arg.partition("=") #partition 把字符串分成三份 第一份:操作符之前，第二份：操作符， 第三份：操作符之后
		name = name.replace('-', '_')
		if not name in self._options: #如果命令行key不在options中,报错
			self.print_help()
			raise Error('Unrecognized command line option: %r' %name)
		option = self._options[name]
		if not equals:
			if option.type == bool:
				value = "true"
			else:
				raise Error('Options %r require a value' %name)

		options.parse(value)
	if final:
		self.run_parse_callbacks()

	return remaining
