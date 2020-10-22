from ipycanvas import MultiCanvas, Canvas, hold_canvas



class smartiS():
    
    def __init__(self, canvases, width, height):
        
        """ Initialisiert die smartiS-Instanz.
        
        canvases <list (string)>: Liste mit Bezeichnungen der Canvas/Ebenen
                     width <int>: Breite des Canvas
                    height <int>: Höhe des Canvas
        """
        
        self.canvas = MultiCanvas(len(canvases), width=width, height=height)
        self.cdict = {}
        for ci in range(len(canvases)):
            self.cdict[canvases[ci]] = self.canvas[ci]
        
        
        
    def __getitem__(self, key):
        
        """ Gibt das Canvas mit angegebenem Namen zurück.
        
        key <string>: Bezeichnung der Ebene (durch __init__ bei Klassenaufruf definiert)
        """
        
        return self.cdict[key]
    
    
    
    # Platz für wiederkehrende benutzerdefinierte Hilfsfunktionen
    
    def draw_arrow(self, layer, xy, angle, length, color="#000000", line_width=2, tip_width=10):
        
        """ Zeichnet einen Pfeil.
        
        layer <ipycanvas.Canvas>: Canvas, in welches der Pfeil gezeichnet werden soll
                      xy <tuple>: Koordinaten (Ende des Pfeilsschaftes)
                   angle <float>: Winkel (Gradmaß)
                  length <float>: Gesamtlänge
                  color <string>: Farbe (Hexadezimalcode, wie HTML)
              line_width <float>: Breite des Pfeilschaftes
               tip_width <float>: Breite der Pfeilspitze
        """
        
        sin_a = sin((angle + 90) * pi / 180)
        cos_a = cos((angle + 90) * pi / 180)

        if length < 15:
            tip_length = 15 + (length - 15)
            width = tip_width / 2 * length / 15
        else:
            tip_length = 15
            width = tip_width / 2
        line_end = (xy[0] + (length - tip_length) * sin_a,
                    xy[1] + (length - tip_length) * cos_a)        
        
        with hold_canvas(layer):
            
            # Pfeilschaft
            layer.line_width = line_width
            layer.stroke_style = color
            layer.fill_style   = color
            layer.begin_path()
            layer.move_to(xy[0], xy[1])
            layer.line_to(line_end[0], line_end[1])
            layer.stroke()
            layer.close_path()
            
            # Pfeilspitze
            layer.move_to(xy[0] + length * sin_a,
                          xy[1] + length * cos_a)
            layer.line_to(line_end[0] + width * sin((angle + 180) * pi / 180),
                          line_end[1] + width * cos((angle + 180) * pi / 180)
                          )
            layer.line_to(line_end[0] - width * sin((angle + 180) * pi / 180),
                          line_end[1] - width * cos((angle + 180) * pi / 180)
                          )
            layer.fill()