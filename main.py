import compiler
filetype="standard/.mth"
runner = compiler.MythCompiler(filetype)
runner.Run("tests.mth")