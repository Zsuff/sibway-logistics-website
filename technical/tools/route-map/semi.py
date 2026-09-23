# Сідельний тягач + напівпричіп (20 т), дивиться праворуч. Габарит ~0..84 x 0..27, колеса на y=23.
def semi(V='#29265b',B='#189cd9',BS='#e8f6fc',D='#201d48'):
    w=lambda cx: f'<circle cx="{cx}" cy="23" r="3.4" fill="{D}" stroke="#fff" stroke-width="1.5"/>'
    return (f'<g><rect x="0" y="0" width="58" height="20" rx="2" fill="{V}"/>'
            f'<rect x="4" y="4" width="50" height="3" rx="1.5" fill="{B}"/>'
            f'<path d="M3 13h52" stroke="#fff" stroke-width=".8" opacity=".18"/>'
            f'<rect x="54" y="18.5" width="28" height="3" rx="1" fill="{D}"/>'
            f'<path d="M61 5h12.5a3 3 0 0 1 2.7 1.7l4.6 10.1a3 3 0 0 1 .2 1.2V21H61z" fill="{V}"/>'
            f'<path d="M65 8h8.3l3.5 7.8H65z" fill="{BS}"/>'
            f'<rect x="59" y="3" width="3" height="16" rx="1" fill="{V}"/>'
            f'{w(9)}{w(17)}{w(25)}{w(63)}{w(76)}</g>')
