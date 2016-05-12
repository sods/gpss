import matplotlib.pyplot as plt
import numpy as np

def plot_matrix(A, ax=None,
                bracket_width=3,
                bracket_style='square',
                type='values',
                colormap=False,
                highlight=False,
                highlight_row=None,
                highlight_col=None,
                highlight_width=3,
                highlight_color=[0,0,0],
                zoom=False,
                zoom_row=None,
                zoom_col=None,
                bracket_color=[0,0,0]):
    """Plot a matrix for visualisation in a slide or piece of text."""
    
    if ax is None:
        ax = plt.gca()
        
    nrows, ncols = A.shape
    
  
    x_lim = np.array([-0.75, ncols-0.25])
    y_lim = np.array([-0.75, nrows-0.25])
  
    ax.cla()
    handle=[]
    if type == 'image':
        handle =  ax.matshow(A)
    elif type == 'imagesc':
        handle =  ax.images(A, [np.array([A.min(), 0]).min(), A.max()])
    elif type == 'values':
        for i in range(nrows):
            for j in range(ncols):
                handle.append(ax.text(j, i, str(A[i, j]), horizontalalignment='center'))
    elif type == 'entries':
        for i in range(nrows):
            for j in range(ncols):
                if isstr(A[i,j]):
                    handle.append(ax.text(j, i, A[i, j], horizontalalignment='center'))
                    
                else:  
                    handle.append(ax.text(j+1, i+1, ' ', horizontalalignment='center'))
    elif type == 'patch':
        for i in range(nrows):
            for j in range(ncols):
                handle.append(ax.add_patch(
                    plt.Rectangle([i-0.5, j-0.5],
                                  width=1., height=1.,
                                  color=(A[i, j])*np.array([1, 1, 1]))))
    elif type == 'colorpatch':
        for i in range(nrows):
            for j in range(ncols):
                handle.append(ax.add_patch(
                    plt.Rectangle([i-0.5, j-0.5],
                                  width=1., height=1.,
                                  color=np.array([A[i, j, 0],
                                                  A[i, j, 1],
                                                  A[i, j, 2]]))))
                
                
    if bracket_style == 'boxes':
        x_lim = np.array([-0.5, ncols-0.5])
        ax.set_xlim(x_lim)
        y_lim = np.array([-0.5, nrows-0.5])
        ax.set_ylim(y_lim)
        for i in range(nrows+1):
            ax.add_line(plt.axhline(y=i-.5, #xmin=-0.5, xmax=ncols-0.5, 
                 color=bracket_color))
        for j in range(ncols+1):
            ax.add_line(plt.axvline(x=j-.5, #ymin=-0.5, ymax=nrows-0.5, 
                 color=bracket_color))
    elif bracket_style == 'square':
        tick_length = 0.25
        ax.plot([x_lim[0]+tick_length,
                     x_lim[0], x_lim[0],
                     x_lim[0]+tick_length],
                    [y_lim[0], y_lim[0],
                     y_lim[1], y_lim[1]],
                    linewidth=bracket_width,
                    color=np.array(bracket_color))
        ax.plot([x_lim[1]-tick_length, x_lim[1],
                              x_lim[1], x_lim[1]-tick_length],
                             [y_lim[0], y_lim[0], y_lim[1],
                              y_lim[1]],
                             linewidth=bracket_width, color=np.array(bracket_color))
      
    if highlight:       
        h_row = highlight_row
        h_col = highlight_col
        if isinstance(h_row, str) and h_row == ':':
            h_row = [0, nrows]
        if isinstance(h_col, str) and h_col == ':':
            h_col = [0, ncols]
        if len(h_row) == 1:
            h_row = [h_row, h_row]
        if len(h_col) == 1:
            h_col = [h_col, h_col]
        h_col.sort()
        h_row.sort()
        ax.add_line(plt.Line2D([h_col[0]-0.5, h_col[0]-0.5,
                              h_col[1]+0.5, h_col[1]+0.5,
                              h_col[0]-0.5],
                             [h_row[0]-0.5, h_row[1]+0.5,
                              h_row[1]+0.5, h_row[0]-0.5,
                              h_row[0]-0.5], color=highlight_color,
                               linewidth=highlight_width))
                    
    if zoom:      
        z_row = zoom_row
        z_col = zoom_col
        if isinstance(z_row, str) and z_row == ':':
            z_row = [1, nrows]
        if isinstance(z_col, str) and z_col == ':':
            z_col = [1, ncols]
        if len(z_row) == 1:
            z_row = [z_row, z_row]
        if len(z_col) == 1:
            z_col = [z_col, z_col]
        z_col.sort()
        z_row.sort()
        x_lim = [z_col[0]-0.5, z_col[1]+0.5]
        y_lim = [z_row[0]-0.5, z_row[1]+0.5]

    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    ax.set_aspect('equal')
    ax.set_frame_on(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.invert_yaxis() #axis ij, axis equal, axis off

    if colormap:
        plt.colormap(obj=options.colormap) 
             
    return handle 


def base_plot(K, ind=[0, 1], ax=None,
              contour_color=[0., 0., 1],
              contour_style='-',
              contour_size=4,
              contour_markersize=4,
              contour_marker='x',
              fontsize=20):
    """
    % BASEPLOT Plot the contour of the covariance.
    % FORMAT
    % DESC creates the basic plot.
    % """

    blackcolor = [0,0,0]
    if ax is None:
        ax = plt.gca()
    v, U = np.linalg.eig(K[ind][:, ind])
    r = np.sqrt(v)
    theta = np.linspace(0, 2*np.pi, 200)[:, None]
    xy = np.dot(np.concatenate([r[0]*np.sin(theta), r[1]*np.cos(theta)], axis=1),U.T)
    cont = plt.Line2D(xy[:, 0], xy[:, 1],
                      linewidth=contour_size,
                      linestyle=contour_style,
                      color=contour_color)
    cent = plt.Line2D([0.], [0.],
                      marker=contour_marker,
                      color=contour_color,
                      linewidth=contour_size,
                      markersize=contour_markersize)

    ax.add_line(cont)
    ax.add_line(cent)

    thandle = []
    thandle.append(ax.set_xlabel('$f_{' + str(ind[1]+1)+ '}$',
                   fontsize=fontsize))
    thandle.append(ax.set_ylabel('$f_{' + str(ind[0]+1)+ '}$',
                   fontsize=fontsize))
    
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    x_lim = [-1.5, 1.5]
    y_lim = [-1.5, 1.5]
    ax.set_xlim(x_lim)
    ax.set_ylim(y_lim)
    
    ax.add_line(plt.Line2D(x_lim, [0, 0], color=blackcolor))
    ax.add_line(plt.Line2D([0, 0], y_lim, color=blackcolor))

    ax.set_aspect('equal')
    #zeroAxes(gca, 0.025, 18, 'times')
    
    return cont, thandle, cent 

def plot_two_point_pred(K, f, x, ax=None, ind=[0, 1],
                        conditional_linestyle = '-',
                        conditional_linecolor = [1., 0., 0.],
                        conditional_size = 4,
                        fixed_linestyle = '-',
                        fixed_linecolor = [0., 1., 0.],
                        fixed_size = 4,stub=None, start=0):
    
    subK = K[ind][:, ind]
    f = f[ind]
    x = x[ind]

    if ax is None:
        ax = plt.gca()

    cont, t, cent = base_plot(K, ind, ax=ax)
    if stub is not None:
        plt.savefig('./diagrams/' + stub + str(start) + '.svg')

    x_lim = ax.get_xlim()
    cont2 = plt.Line2D([x_lim[0], x_lim[1]], [f[0], f[0]], linewidth=fixed_size, linestyle=fixed_linestyle, color=fixed_linecolor)
    ax.add_line(cont2)

    if stub is not None:
        plt.savefig('./diagrams/' + stub + str(start+1) + '.svg')

    # # Compute conditional mean and variance
    f2_mean = subK[0, 1]/subK[0, 0]*f[0]
    f2_var = subK[1, 1] - subK[0, 1]/subK[0, 0]*subK[0, 1]
    x_val = np.linspace(x_lim[0], x_lim[1], 200)
    pdf_val = 1/np.sqrt(2*np.pi*f2_var)*np.exp(-0.5*(x_val-f2_mean)*(x_val-f2_mean)/f2_var)
    pdf = plt.Line2D(x_val, pdf_val+f[0], linewidth=conditional_size, linestyle=conditional_linestyle, color=conditional_linecolor)
    ax.add_line(pdf)
    if stub is not None:
        plt.savefig('./diagrams/' + stub + str(start+2) + '.svg')
    
    obs = plt.Line2D([f[1]], [f[0]], linewidth=10, markersize=10, color=fixed_linecolor, marker='o')
    ax.add_line(obs)
    if stub is not None:
        plt.savefig('./diagrams/' + stub + str(start+3) + '.svg')
    
    # load gpdistfunc

    #printLatexText(['\mappingFunction_1=' numsf2str(f[0], 3)], 'inputValueF1.tex', '../../../gp/tex/diagrams')


def kern_circular_sample(mu, K, filename=None, ax=None, num_samps=5, num_theta=200):

    """% KERNCIRCULARSAMPLE Sample from covariance in a circular way alla Hennig.
    %
    % FORMAT
    % DESC samples from GP along elipses of equiprobability
    % ARG mu : mean of GP.
    % ARG K : covariance of GP.
    % ARG num_samps : number of samples from the Gaussian process.
    % RETURN includeText : the text used to include in latex.
    %
    % SEEALSO : kernCreate
    %
    % COPYRIGHT: Neil D. Lawrence, 2013
    
    % GPMAT"""

    tau = 2*np.pi
    n = K.shape[0]


    R1 = np.random.normal(size=(n, num_samps))
    U1 = np.dot(R1,np.diag(1/np.sqrt(np.sum(R1*R1, axis=0))))
    R2 = np.random.normal(size=(n, num_samps))
    R2 = R2 - np.dot(U1,np.diag(np.sum(R2*U1, axis=0)))
    R2 = np.dot(R2,np.diag(np.sqrt(np.sum(R1*R1, axis=0))/np.sqrt(np.sum(R2*R2, axis=0))))
    L = np.linalg.cholesky(K+np.diag(np.ones((n)))*1e-6)


    from matplotlib import animation
    x_lim = (0, 1)
    y_lim = (-2, 2)
    if ax is None:
        ax = plt.axes(xlim=x_lim, ylim=y_lim)
    else:
        ax.set_xlim(x_lim)
        ax.set_ylim(y_lim)
    line = []
    for i in range(num_samps):
        l, = ax.plot([], [], lw=2)
        line.append(l)
        
    # initialization function: plot the background of each frame
    def init():
        for i in range(num_samps):
            line[i].set_data([], [])
        return line,

    # animation function.  This is called sequentially
    def animate(i):
        theta = float(i)/num_theta*tau
        xc = np.cos(theta)
        yc = np.sin(theta)
        # generate 2d basis in t-d space
        coord = xc*R1 + yc*R2
        y = np.dot(L,coord)
        x = np.linspace(0, 1, n)
        for i in range(num_samps):
            line[i].set_data(x, y[:, i])
        return line,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=num_theta, blit=True)
    if filename is not None:
        anim.save('./diagrams/' + filename, writer='imagemagick', fps=30)
