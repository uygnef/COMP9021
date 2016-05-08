from tangram import *

def testing():
    '''
    >>> file = open ('pieces_A.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    True
    >>> file = open ('pieces_AA.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    True
    >>> file = open ('incorrect_pieces_1.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    False
    >>> file = open ('incorrect_pieces_2.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    False
    >>> file = open ('incorrect_pieces_3.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    False
    >>> file = open ('incorrect_pieces_4.xml')
    >>> coloured_pieces = available_coloured_pieces ( file )
    >>> are_valid ( coloured_pieces )
    False
    >>> file = open ('pieces_A.xml')
    >>> coloured_pieces_1 = available_coloured_pieces ( file )
    >>> file = open ('pieces_AA.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    True
    >>> file = open ('shape_A_1.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    False
    >>> file = open ('tangram_B_a.xml')
    >>> coloured_pieces_1 = available_coloured_pieces ( file )
    >>> file = open ('tangram_B_b.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    True
    >>> file = open ('tangram_B_c.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    True
    >>> file = open ('tangram_B_d.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    True
    >>> file = open ('tangram_B.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    True
    >>> file = open ('tangram_C.xml')
    >>> coloured_pieces_2 = available_coloured_pieces ( file )
    >>> are_identical_sets_of_coloured_pieces ( coloured_pieces_1 ,coloured_pieces_2 )
    False
    >>> file = open ('shape_B.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_B_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_B_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_B_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_B_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_B.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_C.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_C.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_C_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_C_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_C_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_C_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_D.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_D_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_D_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_D_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_D_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_E.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_E.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_F.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_F.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_F_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_J.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_J.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_J_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_J_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_J_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_J_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_H.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_H.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_H_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_H_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_H_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_H_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_I.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_I.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_I_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_I_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_I_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_I_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_K.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_K.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_K_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_K_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_K_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_K_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_L.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_L.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_L_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_L_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_L_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_M.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_M_e.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_M_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_M_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_M_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_M_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('shape_O.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_O.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_O_a.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_O_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_O_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_O_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    True
    >>> file = open ('tangram_O_e.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('tangram_I.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('tangram_H_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('tangram_B_b.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('tangram_C_c.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('tangram_H_d.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    >>> file = open ('shape_Z.xml')
    >>> shape = available_coloured_pieces ( file )
    >>> file = open ('tangram_Z.xml')
    >>> tangram = available_coloured_pieces ( file )
    >>> is_solution ( tangram , shape )
    False
    '''
if __name__ == '__main__':
    import doctest
    doctest.testmod()