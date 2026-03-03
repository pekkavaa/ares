auto CPU::EMUX(cr64& rt, s16 imm) -> void {
  if (imm == 0x1f2) {
    // printf("fast nop\n");
    CPU::step(64 * 2);
  }
}