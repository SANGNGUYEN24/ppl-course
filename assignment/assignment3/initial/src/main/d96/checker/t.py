    def visitVarDecl(self, ast, o):
        frame = o.frame
        if frame:
            tempSymbol = Symbol(ast.name, ast.typ, Index(frame.getCurrIndex()))
            self.emit.printout(
                self.emit.emitVAR(frame.getCurrIndex(), ast.name, ast.typ, frame.getStartLabel(), frame.getEndLabel()))
            frame.getNewIndex()
            return tempSymbol
        else:
            tempSymbol = Symbol(ast.name, ast.typ, CName(self.className))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.name, ast.typ, False, None))
            return tempSymbol