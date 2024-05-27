for bomba in lista_b:
        if bomba.rect.colliderect(casa.rect) == True:
            pygame.quit()
            exit()